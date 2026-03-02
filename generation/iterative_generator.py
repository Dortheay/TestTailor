"""
Iterative Coverage Improvement
================================
Stage 3 of TestTailor: the generate-and-refine loop.

For each uncovered unit, the loop:
  1. Builds the initial prompt (stages 1 + 2 already done).
  2. Calls the LLM.
  3. Extracts and executes the generated test.
  4. On success → done.
  5. On compilation/runtime error → build repair prompt and retry.
  6. On 'runs but misses coverage' → if test reaches the function,
     treat it as a new path-proximal seed and refine; else discard and retry.
  7. Repeat up to max_iterations_per_unit times.

Paper: "each unit is allotted at most three iterations"
"""

import ast
import logging
from typing import Dict, List, Optional, Set

from config import TestTailorConfig
from models import (
    CodeUnit, DependencyContext, ExecutionPath,
    GeneratedTest, PathProximalTest, TargetPath
)
from generation.llm_client import LLMClient, extract_code
from generation.prompt_builder import (
    build_initial_prompt,
    build_repair_prompt,
    build_refine_prompt,
)
from execution.test_executor import TestExecutor
from path_analysis.path_divergence import PathDivergenceAnalyzer

logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────────────
# Iterative Generator
# ──────────────────────────────────────────────────────────────────────────────

class IterativeGenerator:
    """
    Orchestrates the generate → execute → repair/refine loop for one CodeUnit.
    """

    def __init__(
        self,
        config: TestTailorConfig,
        llm_client: LLMClient,
        executor: TestExecutor,
        source: str,
    ):
        self.config = config
        self.llm = llm_client
        self.executor = executor
        self.source = source
        self._div_analyzer = PathDivergenceAnalyzer(source)

    def generate(
        self,
        unit: CodeUnit,
        ctx: DependencyContext,
        target_path: TargetPath,
        proximal: Optional[PathProximalTest],
        baseline_covered: Set[int],
    ) -> List[GeneratedTest]:
        """
        Try to cover *unit* in up to max_iterations_per_unit attempts.

        Returns
        -------
        All GeneratedTest objects produced (regardless of success).
        """
        max_iter = self.config.max_iterations_per_unit
        results: List[GeneratedTest] = []

        # Build the initial prompt once
        current_prompt = build_initial_prompt(ctx, target_path, proximal)
        current_proximal = proximal

        for iteration in range(1, max_iter + 1):
            logger.info(
                "  [unit %s] iteration %d/%d", unit.unit_id, iteration, max_iter
            )

            # ── Step 1: call LLM ─────────────────────────────────────────
            try:
                llm_response = self.llm.complete(current_prompt)
            except Exception as exc:
                logger.warning("  LLM call failed: %s", exc)
                break

            raw_code = extract_code(llm_response.content)
            if raw_code is None:
                logger.warning("  Could not extract code from LLM response.")
                continue

            # ── Step 2: execute ──────────────────────────────────────────
            result = self.executor.execute(
                raw_code, unit, baseline_covered, iteration=iteration
            )
            results.append(result)

            # ── Step 3: evaluate ─────────────────────────────────────────
            if result.covers_target:
                logger.info("  ✓ Target unit covered on iteration %d", iteration)
                break

            if result.compilation_error:
                logger.info("  ✗ Compilation error – building repair prompt")
                current_prompt = build_repair_prompt(
                    current_prompt, raw_code, result.compilation_error
                )
                continue

            if result.runtime_error:
                logger.info("  ✗ Runtime error – building repair prompt")
                current_prompt = build_repair_prompt(
                    current_prompt, raw_code, result.runtime_error
                )
                continue

            # Test ran successfully but missed the target
            if result.executed:
                if result.reaches_function:
                    logger.info(
                        "  ~ Ran but missed target – treating as new proximal seed"
                    )
                    # Elevate this test to a new proximal seed
                    new_ep = ExecutionPath(
                        test_id=f"generated_iter_{iteration}",
                        test_source=raw_code,
                        covered_lines=result.newly_covered_lines | baseline_covered,
                    )
                    new_proximal = PathProximalTest(
                        test_id=new_ep.test_id,
                        test_source=raw_code,
                        execution_path=new_ep,
                        jaccard_similarity=0.0,
                    )
                    # Re-analyze divergence with the new proximal
                    new_proximal = self._div_analyzer.analyze(
                        new_proximal, target_path
                    )
                    current_prompt = build_refine_prompt(
                        current_prompt, raw_code, new_proximal, target_path
                    )
                    current_proximal = new_proximal
                else:
                    logger.info(
                        "  ~ Test did not reach the function – regenerate"
                    )
                    # Keep the original prompt; just retry

        return results


# ──────────────────────────────────────────────────────────────────────────────
# Module-level orchestrator
# ──────────────────────────────────────────────────────────────────────────────

class ModuleOrchestrator:
    """
    Runs the full TestTailor pipeline for one Python module.
    Called by the top-level main.py.
    """

    def __init__(
        self,
        config: TestTailorConfig,
        llm_client: LLMClient,
        source_file: str,
        project_root: str,
    ):
        self.config = config
        self.llm = llm_client
        self.source_file = source_file
        self.project_root = project_root
        self.source = open(source_file, encoding="utf-8").read()
        self.executor = TestExecutor(
            source_file, timeout=config.test_timeout_seconds
        )
        self.generator = IterativeGenerator(
            config, llm_client, self.executor, self.source
        )

    def run(
        self,
        units: List[CodeUnit],
        dependency_ctxs: Dict[str, DependencyContext],
        target_paths: Dict[str, TargetPath],
        proximal_tests: Dict[str, Optional[PathProximalTest]],
        baseline_covered: Set[int],
    ) -> List[GeneratedTest]:
        """
        Iterate over all uncovered units, generate tests, and return results.
        """
        all_results: List[GeneratedTest] = []
        current_covered = set(baseline_covered)

        for unit in units:
            uid = unit.unit_id

            # Skip if already covered by a previously generated test
            unit_lines = set(range(unit.start_lineno, unit.end_lineno + 1))
            if unit_lines.issubset(current_covered):
                logger.info("Unit %s already covered – skipping", uid)
                continue

            ctx = dependency_ctxs.get(uid)
            t_path = target_paths.get(uid)
            proximal = proximal_tests.get(uid)

            if ctx is None or t_path is None:
                logger.warning("Missing context or target path for unit %s", uid)
                continue

            logger.info("Processing unit %s (lines %d-%d)",
                        uid, unit.start_lineno, unit.end_lineno)

            results = self.generator.generate(
                unit, ctx, t_path, proximal, current_covered
            )
            all_results.extend(results)

            # Update baseline for subsequent units
            for r in results:
                if r.executed:
                    current_covered |= r.newly_covered_lines

        return all_results
