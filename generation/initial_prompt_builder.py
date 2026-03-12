"""
Initial Prompt Builder
======================
High-level entry point that auto-constructs the initial LLM prompt
for a given target line in a source file.

Given:
  - target_file   : path to the Python module under test
  - function_name : name of the function containing the target line
  - target_line   : start line number of the uncovered code unit
  - project_root  : project root for cross-file dependency resolution
  - end_line      : (optional) end line; defaults to target_line
  - tests_dir     : (optional) directory with existing test_*.py files
                    used to identify the path-proximal test
  - test_sources  : (optional) Dict[test_id → source] – alternative to tests_dir

Pipeline stages performed automatically:
  1. Build CodeUnit (with code_snippet extracted from source)
  2. DependencyCollector  → DependencyContext
  3. SymbolicConstraintExtractor → TargetPath (path constraints)
  4. (if test sources given) collect execution traces →
       PathProximalSelector → PathDivergenceAnalyzer → PathProximalTest
  5. build_initial_prompt(ctx, target_path, proximal) → prompt string
"""

import argparse
import os
import textwrap
from pathlib import Path
from typing import Dict, Optional

from models import CodeUnit, PathProximalTest
from preprocessing.dependency_collector import DependencyCollector
from path_analysis.symbolic_executor import SymbolicConstraintExtractor
from path_analysis.path_proximal import PathProximalSelector
from path_analysis.path_divergence import PathDivergenceAnalyzer
from execution.trace_collector import collect_test_suite_traces
from generation.prompt_builder import build_initial_prompt


# ──────────────────────────────────────────────────────────────────────────────
# Internal helpers
# ──────────────────────────────────────────────────────────────────────────────

def _extract_snippet(source_lines: list, start: int, end: int) -> str:
    """Extract and dedent source lines [start..end] (1-indexed, inclusive)."""
    lines = source_lines[start - 1 : end]
    return textwrap.dedent("\n".join(lines))


def _load_tests_from_dir(tests_dir: str) -> Dict[str, str]:
    """Load all test_*.py files from a directory as {stem: source} dict."""
    tests_path = Path(tests_dir)
    if not tests_path.exists():
        return {}
    return {
        p.stem: p.read_text(encoding="utf-8")
        for p in tests_path.glob("test_*.py")
    }


def _find_proximal(
    unit: CodeUnit,
    source: str,
    target_path,
    target_file: str,
    test_sources: Dict[str, str],
) -> Optional[PathProximalTest]:
    """
    Collect traces, select the path-proximal test, and run divergence analysis.
    Returns None if no suitable test is found.
    """
    traces = collect_test_suite_traces(test_sources, target_file)
    if not traces:
        return None

    selector = PathProximalSelector(target_file, unit.function_name)
    result = selector.select_best_test(unit, traces)
    if result is None:
        return None

    best_id, score = result
    best_trace = traces[best_id]
    proximal = PathProximalTest(
        test_id=best_id,
        test_source=best_trace.test_source,
        execution_path=best_trace,
        jaccard_similarity=score,
    )

    analyzer = PathDivergenceAnalyzer(source)
    return analyzer.analyze(proximal, target_path)


# ──────────────────────────────────────────────────────────────────────────────
# Stateful builder (reuses parsed state across multiple calls on one file)
# ──────────────────────────────────────────────────────────────────────────────

class InitialPromptBuilder:
    """
    Stateful builder for constructing initial prompts from a single target file.

    Caches the parsed source, dependency index, and AST so that multiple
    ``build()`` calls on different lines of the same file are efficient.

    Parameters
    ----------
    target_file  : Path to the Python module under test.
    project_root : Root directory used for cross-file dependency resolution.
    """

    def __init__(self, target_file: str, project_root: str):
        self.target_file = os.path.realpath(target_file)
        self.project_root = project_root
        self.source = Path(self.target_file).read_text(encoding="utf-8")
        self._source_lines = self.source.splitlines()

        # Pre-built components (shared across build() calls)
        self._dep_collector = DependencyCollector(self.target_file, project_root)
        self._sym_extractor = SymbolicConstraintExtractor(self.source)
        self._div_analyzer  = PathDivergenceAnalyzer(self.source)

    def build(
        self,
        function_name: str,
        target_line: int,
        end_line: Optional[int] = None,
        unit_type: str = "linear",
        tests_dir: Optional[str] = None,
        test_sources: Optional[Dict[str, str]] = None,
    ) -> str:
        """
        Build the initial generation prompt for a specific uncovered target line.

        Parameters
        ----------
        function_name : Name of the enclosing function.
        target_line   : Start line (1-indexed) of the uncovered code unit.
        end_line      : End line (1-indexed). Defaults to *target_line*.
        unit_type     : CodeUnit type hint – "linear" | "branch" | "loop".
        tests_dir     : Directory containing existing test_*.py files.
                        Used for path-proximal test selection.
        test_sources  : Dict[test_id → source] – alternative to *tests_dir*.
                        If both are given, *test_sources* takes precedence.

        Returns
        -------
        str  The fully assembled initial prompt, ready to send to the LLM.
        """
        if end_line is None:
            end_line = target_line

        # ── Stage 1: CodeUnit ────────────────────────────────────────────────
        snippet = _extract_snippet(self._source_lines, target_line, end_line)
        unit = CodeUnit(
            unit_id=f"{function_name}:{target_line}-{end_line}",
            source_file=self.target_file,
            function_name=function_name,
            start_lineno=target_line,
            end_lineno=end_line,
            unit_type=unit_type,
            code_snippet=snippet,
        )

        # ── Stage 2: Dependency context ──────────────────────────────────────
        ctx = self._dep_collector.collect(unit)

        # ── Stage 3: Symbolic path constraints ───────────────────────────────
        target_path = self._sym_extractor.extract(unit)

        # ── Stage 4: Path-proximal test (optional) ───────────────────────────
        proximal: Optional[PathProximalTest] = None

        # test_sources kwarg overrides tests_dir
        if test_sources is None and tests_dir is not None:
            test_sources = _load_tests_from_dir(tests_dir)

        if test_sources:
            proximal = _find_proximal(
                unit, self.source, target_path, self.target_file, test_sources
            )

        # ── Stage 5: Assemble prompt ─────────────────────────────────────────
        return build_initial_prompt(ctx, target_path, proximal)


# ──────────────────────────────────────────────────────────────────────────────
# Stateless convenience function
# ──────────────────────────────────────────────────────────────────────────────

def build_initial_prompt_for_target(
    target_file: str,
    function_name: str,
    target_line: int,
    project_root: str,
    end_line: Optional[int] = None,
    unit_type: str = "linear",
    tests_dir: Optional[str] = None,
    test_sources: Optional[Dict[str, str]] = None,
) -> str:
    """
    Stateless convenience wrapper around :class:`InitialPromptBuilder`.

    Constructs a one-shot builder, calls ``build()``, and returns the prompt.
    Prefer :class:`InitialPromptBuilder` when generating prompts for multiple
    lines in the same file.

    Parameters
    ----------
    target_file   : Path to the Python module under test.
    function_name : Name of the function containing the target line.
    target_line   : Start line (1-indexed) of the uncovered code unit.
    project_root  : Root directory for cross-file dependency resolution.
    end_line      : End line (1-indexed). Defaults to *target_line*.
    unit_type     : "linear" | "branch" | "loop".
    tests_dir     : Directory containing existing test_*.py files.
    test_sources  : Dict[test_id → source] – alternative to *tests_dir*.

    Returns
    -------
    str  The assembled initial prompt string.
    """
    builder = InitialPromptBuilder(target_file, project_root)
    return builder.build(
        function_name=function_name,
        target_line=target_line,
        end_line=end_line,
        unit_type=unit_type,
        tests_dir=tests_dir,
        test_sources=test_sources,
    )


# ──────────────────────────────────────────────────────────────────────────────
# CLI entry point
# ──────────────────────────────────────────────────────────────────────────────

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Auto-construct the initial LLM prompt for a target uncovered line.\n\n"
            "Example:\n"
            "  python -m generation.initial_prompt_builder \\\n"
            "      --file tests/order_management/service/order_service.py \\\n"
            "      --func create_order \\\n"
            "      --start-line 42 \\\n"
            "      --project-root tests/order_management \\\n"
            "      --tests-dir tests/order_management/tests/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--file",       required=True, help="Target Python source file")
    parser.add_argument("--func",       required=True, help="Target function name")
    parser.add_argument("--start-line", required=True, type=int, help="Start line (1-indexed)")
    parser.add_argument("--end-line",   type=int,      default=None, help="End line (default: same as start-line)")
    parser.add_argument("--project-root", required=True, help="Project root directory")
    parser.add_argument("--unit-type",  default="linear",
                        choices=["linear", "branch", "loop"],
                        help="CodeUnit type annotation (default: linear)")
    parser.add_argument("--tests-dir",  default=None,
                        help="Directory with existing test_*.py files for path-proximal selection")
    parser.add_argument("--output",     default=None,
                        help="Write the prompt to this file instead of stdout")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    prompt = build_initial_prompt_for_target(
        target_file=args.file,
        function_name=args.func,
        target_line=args.start_line,
        project_root=args.project_root,
        end_line=args.end_line,
        unit_type=args.unit_type,
        tests_dir=args.tests_dir,
    )

    if args.output:
        Path(args.output).write_text(prompt, encoding="utf-8")
        print(f"[✓] Prompt written to: {args.output}")
    else:
        print(prompt)


if __name__ == "__main__":
    main()
