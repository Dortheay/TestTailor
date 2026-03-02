"""
TestTailor — Main Entry Point
==============================
Orchestrates the three-stage pipeline for one or more Python modules:

  Stage 1  Contextual Pre-Processing
           ├── Unit Partition
           └── Dependency Collection

  Stage 2  Fine-Grained Path Analysis
           ├── Constraints Extraction (symbolic execution)
           ├── Path-Proximal Test Selection (Algorithm 1)
           └── Path Divergence Analysis

  Stage 3  Iterative Coverage Improvement
           └── generate → execute → repair/refine (≤3 iterations per unit)

Usage
-----
    python -m testtailor.main \
        --module  path/to/module.py \
        --tests   path/to/initial_tests/ \
        --project path/to/project_root \
        --model   gpt-4o-2024-11-20 \
        --api-key sk-...

Or use the Python API:

    from testtailor.main import run_testtailor
    results = run_testtailor(module_path, test_dir, project_root, config)
"""

import argparse
import ast
import logging
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

from config import TestTailorConfig
from models import (
    CodeUnit, DependencyContext, GeneratedTest,
    ModuleResult, PathProximalTest, TargetPath
)

# Stage 1
from preprocessing.unit_partition import partition_uncovered
from preprocessing.dependency_collector import collect_dependencies

# Stage 2
from path_analysis.symbolic_executor import extract_constraints
from path_analysis.path_proximal import find_path_proximal_test
from path_analysis.path_divergence import analyze_divergence
from execution.trace_collector import collect_test_suite_traces

# Stage 3
from generation.llm_client import LLMClient
from generation.iterative_generator import ModuleOrchestrator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("testtailor")


# ──────────────────────────────────────────────────────────────────────────────
# Pipeline helpers
# ──────────────────────────────────────────────────────────────────────────────

def _load_test_sources(test_dir: str) -> Dict[str, str]:
    """Load all .py test files from *test_dir* as a dict {test_id: source}."""
    sources: Dict[str, str] = {}
    for path in Path(test_dir).rglob("test_*.py"):
        sources[str(path)] = path.read_text(encoding="utf-8")
    for path in Path(test_dir).rglob("*_test.py"):
        if str(path) not in sources:
            sources[str(path)] = path.read_text(encoding="utf-8")
    return sources


def _get_uncovered_lines(
    source_file: str,
    test_sources: Dict[str, str],
) -> Set[int]:
    """
    Determine which lines of *source_file* are uncovered by the existing tests.
    Uses simple in-process tracing.
    """
    from execution.trace_collector import TraceCollector

    covered: Set[int] = set()
    for test_id, src in test_sources.items():
        collector = TraceCollector(source_file)
        ns: dict = {}
        try:
            code = compile(src, test_id, "exec")
            with collector:
                exec(code, ns)
            import unittest, io
            loader = unittest.TestLoader()
            suite = unittest.TestSuite()
            for name, obj in ns.items():
                if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                    suite.addTests(loader.loadTestsFromTestCase(obj))
            runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0)
            with collector:
                runner.run(suite)
        except Exception:
            pass
        covered |= collector.covered_lines

    # All executable lines in the module
    source = Path(source_file).read_text(encoding="utf-8")
    tree = ast.parse(source)
    all_lines: Set[int] = {
        node.lineno for node in ast.walk(tree) if hasattr(node, 'lineno')
    }
    return all_lines - covered


def _find_func_node(source: str, func_name: str) -> Optional[ast.FunctionDef]:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if (isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and
                node.name == func_name):
            return node
    return None


# ──────────────────────────────────────────────────────────────────────────────
# Core pipeline function
# ──────────────────────────────────────────────────────────────────────────────

def run_testtailor(
    module_path: str,
    test_dir: str,
    project_root: str,
    config: TestTailorConfig,
) -> ModuleResult:
    """
    Run the full TestTailor pipeline for *module_path*.

    Parameters
    ----------
    module_path  : path to the Python module under test
    test_dir     : directory containing initial test files
    project_root : root of the project (for cross-file dependency resolution)
    config       : TestTailorConfig with LLM settings, timeouts, etc.
    """
    source = Path(module_path).read_text(encoding="utf-8")

    logger.info("=" * 70)
    logger.info("TestTailor: processing %s", module_path)
    logger.info("=" * 70)

    # ── Load initial test suite ───────────────────────────────────────────
    logger.info("[0] Loading initial test suite from %s", test_dir)
    test_sources = _load_test_sources(test_dir)
    logger.info("    Found %d test files", len(test_sources))

    # ── Measure initial coverage ──────────────────────────────────────────
    logger.info("[0] Measuring initial coverage ...")
    uncovered_lines = _get_uncovered_lines(module_path, test_sources)
    all_executable = {
        node.lineno for node in ast.walk(ast.parse(source))
        if hasattr(node, 'lineno')
    }
    baseline_covered = all_executable - uncovered_lines
    initial_stmt_cov = (
        len(baseline_covered) / len(all_executable) * 100
        if all_executable else 0.0
    )
    logger.info("    Initial statement coverage: %.1f%%", initial_stmt_cov)

    # ── Collect execution traces for all existing tests ───────────────────
    logger.info("[0] Collecting execution traces ...")
    execution_paths = collect_test_suite_traces(test_sources, module_path)

    # ─────────────────────────────────────────────────────────────────────
    # STAGE 1: Contextual Pre-Processing
    # ─────────────────────────────────────────────────────────────────────
    logger.info("[1] Stage 1: Contextual Pre-Processing")

    units = partition_uncovered(module_path, uncovered_lines)
    logger.info("    Partitioned into %d uncovered units", len(units))

    dep_ctxs: Dict[str, DependencyContext] = {}
    for unit in units:
        dep_ctxs[unit.unit_id] = collect_dependencies(
            unit, module_path, project_root
        )

    # ─────────────────────────────────────────────────────────────────────
    # STAGE 2: Fine-Grained Path Analysis
    # ─────────────────────────────────────────────────────────────────────
    logger.info("[2] Stage 2: Fine-Grained Path Analysis")

    target_paths: Dict[str, TargetPath] = {}
    proximal_tests: Dict[str, Optional[PathProximalTest]] = {}

    for unit in units:
        logger.info("    Analyzing unit %s ...", unit.unit_id)

        # 2a. Extract symbolic constraints
        t_path = extract_constraints(unit, source)
        target_paths[unit.unit_id] = t_path

        # 2b. Find path-proximal test
        func_node = _find_func_node(source, unit.function_name)
        if func_node is None:
            proximal_tests[unit.unit_id] = None
            continue

        proximal = find_path_proximal_test(
            unit, t_path, execution_paths, func_node
        )

        # 2c. Path divergence analysis
        if proximal is not None:
            proximal = analyze_divergence(proximal, t_path, source)

        proximal_tests[unit.unit_id] = proximal

    # ─────────────────────────────────────────────────────────────────────
    # STAGE 3: Iterative Coverage Improvement
    # ─────────────────────────────────────────────────────────────────────
    logger.info("[3] Stage 3: Iterative Coverage Improvement")

    llm_client = LLMClient(config)
    orchestrator = ModuleOrchestrator(
        config, llm_client, module_path, project_root
    )

    all_generated = orchestrator.run(
        units=units,
        dependency_ctxs=dep_ctxs,
        target_paths=target_paths,
        proximal_tests=proximal_tests,
        baseline_covered=baseline_covered,
    )

    # ── Compute final coverage ────────────────────────────────────────────
    final_covered = set(baseline_covered)
    for g in all_generated:
        if g.executed:
            final_covered |= g.newly_covered_lines

    final_stmt_cov = (
        len(final_covered) / len(all_executable) * 100
        if all_executable else 0.0
    )
    logger.info("[✓] Final statement coverage: %.1f%%", final_stmt_cov)
    logger.info("    LLM calls: %d  |  API cost: $%.4f",
                llm_client.total_calls, llm_client.total_cost_usd)

    return ModuleResult(
        module_path=module_path,
        initial_statement_coverage=initial_stmt_cov,
        initial_branch_coverage=0.0,  # full branch measurement needs more infra
        final_statement_coverage=final_stmt_cov,
        final_branch_coverage=0.0,
        generated_tests=all_generated,
        llm_calls=llm_client.total_calls,
        api_cost_usd=llm_client.total_cost_usd,
    )


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="TestTailor: high-coverage test generation with LLMs"
    )
    p.add_argument("--module",   required=True,  help="Path to the module under test")
    p.add_argument("--tests",    required=True,  help="Directory of initial test files")
    p.add_argument("--project",  required=True,  help="Project root directory")
    p.add_argument("--model",    default="gpt-4o-2024-11-20",
                   help="LLM model (e.g. gpt-4o-2024-11-20 or deepseek-v3)")
    p.add_argument("--api-key",  default=None,
                   help="API key (or set OPENAI_API_KEY env var)")
    p.add_argument("--api-base", default=None,
                   help="Custom API base URL (for DeepSeek etc.)")
    p.add_argument("--max-iter", type=int, default=3,
                   help="Max repair iterations per unit (default 3)")
    p.add_argument("--output",   default="testtailor_output",
                   help="Output directory for generated tests")
    p.add_argument("--verbose",  action="store_true")
    return p.parse_args()


def main():
    args = _parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    config = TestTailorConfig(
        llm_model=args.model,
        api_key=args.api_key or os.getenv("OPENAI_API_KEY"),
        api_base=args.api_base,
        max_iterations_per_unit=args.max_iter,
        output_dir=args.output,
        verbose=args.verbose,
    )

    result = run_testtailor(
        module_path=args.module,
        test_dir=args.tests,
        project_root=args.project,
        config=config,
    )

    # Save generated tests to output dir
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    successful = [g for g in result.generated_tests if g.covers_target]
    all_executed = [g for g in result.generated_tests if g.executed and not g.covers_target]

    if successful:
        merged = "\n\n".join(g.source for g in successful)
        out_file = out_dir / "generated_tests.py"
        out_file.write_text(merged, encoding="utf-8")
        logger.info("Saved %d coverage-improving tests to %s", len(successful), out_file)

    print("\n" + "=" * 60)
    print("TestTailor Summary")
    print("=" * 60)
    print(f"  Module           : {result.module_path}")
    print(f"  Initial stmt cov : {result.initial_statement_coverage:.1f}%")
    print(f"  Final stmt cov   : {result.final_statement_coverage:.1f}%")
    print(f"  Δ coverage       : +{result.final_statement_coverage - result.initial_statement_coverage:.1f}%")
    print(f"  Generated tests  : {len(result.generated_tests)}")
    print(f"  Covering target  : {len(successful)}")
    print(f"  LLM calls        : {result.llm_calls}")
    print(f"  API cost         : ${result.api_cost_usd:.4f}")


if __name__ == "__main__":
    main()
