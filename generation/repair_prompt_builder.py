"""
Repair Prompt Builder
=====================
Constructs the repair prompt when a generated test has a compilation or
runtime error.  Mirrors the structure of initial_prompt_builder.py.

The repair prompt = initial context (all sections from the initial prompt)
                  + the failed test code block
                  + the error message
                  + repair task instructions

This module can be used in two ways:

1. Standalone (end-to-end):
       builder = RepairPromptBuilder(target_file, project_root)
       prompt  = builder.build(function_name, target_line,
                               failed_test, error_message, error_type)

2. Lightweight wrapper (when initial_prompt already exists):
       from generation.prompt_builder import build_repair_prompt
       prompt = build_repair_prompt(initial_prompt, failed_test,
                                    error_message, error_type)

CLI usage example:
    python -m generation.repair_prompt_builder \\
        --file tests/order_management/service/order_service.py \\
        --func create_order \\
        --start-line 12 --end-line 14 \\
        --project-root tests/order_management \\
        --tests-dir tests/order_management/tests/ \\
        --failed-test path/to/failed_test.py \\
        --error-type compilation \\
        --error "SyntaxError at line 3: invalid syntax"
"""

import argparse
import os
from pathlib import Path
from typing import Dict, Optional

from generation.initial_prompt_builder import InitialPromptBuilder
from generation.prompt_builder import build_repair_prompt


# ──────────────────────────────────────────────────────────────────────────────
# Stateful builder
# ──────────────────────────────────────────────────────────────────────────────

class RepairPromptBuilder:
    """
    Builds repair prompts for a fixed target file.

    Internally holds an :class:`InitialPromptBuilder` so that the source is
    read and parsed only once, even across multiple repair iterations.

    Parameters
    ----------
    target_file  : Path to the Python module under test.
    project_root : Root directory for cross-file dependency resolution.
    """

    def __init__(self, target_file: str, project_root: str):
        self._initial_builder = InitialPromptBuilder(target_file, project_root)

    def build(
        self,
        function_name: str,
        target_line: int,
        failed_test: str,
        error_message: str,
        error_type: str = "compilation",
        end_line: Optional[int] = None,
        unit_type: str = "linear",
        tests_dir: Optional[str] = None,
        test_sources: Optional[Dict[str, str]] = None,
    ) -> str:
        """
        Build the repair prompt for a failing test.

        Parameters
        ----------
        function_name : Name of the enclosing function.
        target_line   : Start line (1-indexed) of the uncovered code unit.
        failed_test   : Source code of the test that failed.
        error_message : Error string from TestExecutor
                        (``compilation_error`` or ``runtime_error``).
        error_type    : ``"compilation"`` or ``"runtime"``.
                        Controls the repair-task wording.
        end_line      : End line (1-indexed). Defaults to *target_line*.
        unit_type     : ``"linear"`` | ``"branch"`` | ``"loop"``.
        tests_dir     : Directory with existing ``test_*.py`` files
                        (used to include a path-proximal test in context).
        test_sources  : Dict[test_id → source] – alternative to *tests_dir*.

        Returns
        -------
        str  The fully assembled repair prompt.
        """
        initial_prompt = self._initial_builder.build(
            function_name=function_name,
            target_line=target_line,
            end_line=end_line,
            unit_type=unit_type,
            tests_dir=tests_dir,
            test_sources=test_sources,
        )
        return build_repair_prompt(
            previous_prompt=initial_prompt,
            previous_test=failed_test,
            error_message=error_message,
            error_type=error_type,
        )


# ──────────────────────────────────────────────────────────────────────────────
# Stateless convenience function
# ──────────────────────────────────────────────────────────────────────────────

def build_repair_prompt_for_target(
    target_file: str,
    function_name: str,
    target_line: int,
    project_root: str,
    failed_test: str,
    error_message: str,
    error_type: str = "compilation",
    end_line: Optional[int] = None,
    unit_type: str = "linear",
    tests_dir: Optional[str] = None,
    test_sources: Optional[Dict[str, str]] = None,
) -> str:
    """
    Stateless convenience wrapper around :class:`RepairPromptBuilder`.

    Prefer :class:`RepairPromptBuilder` when producing multiple repair prompts
    for the same file (avoids re-parsing the source on each call).
    """
    builder = RepairPromptBuilder(target_file, project_root)
    return builder.build(
        function_name=function_name,
        target_line=target_line,
        failed_test=failed_test,
        error_message=error_message,
        error_type=error_type,
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
            "Build the repair prompt for a failing generated test.\n\n"
            "Example:\n"
            "  python -m generation.repair_prompt_builder \\\n"
            "      --file tests/order_management/service/order_service.py \\\n"
            "      --func create_order \\\n"
            "      --start-line 12 --end-line 14 \\\n"
            "      --project-root tests/order_management \\\n"
            "      --tests-dir tests/order_management/tests/ \\\n"
            "      --failed-test /tmp/failed_test.py \\\n"
            "      --error-type compilation \\\n"
            "      --error \"SyntaxError at line 3: invalid syntax\""
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--file",         required=True, help="Target Python source file")
    parser.add_argument("--func",         required=True, help="Target function name")
    parser.add_argument("--start-line",   required=True, type=int, help="Start line (1-indexed)")
    parser.add_argument("--end-line",     type=int, default=None,  help="End line (default: same as start-line)")
    parser.add_argument("--project-root", required=True, help="Project root directory")
    parser.add_argument("--unit-type",    default="linear",
                        choices=["linear", "branch", "loop"],
                        help="CodeUnit type annotation (default: linear)")
    parser.add_argument("--tests-dir",    default=None,
                        help="Directory with existing test_*.py files for path-proximal selection")
    parser.add_argument("--failed-test",  required=True,
                        help="Path to the Python file containing the failing test")
    parser.add_argument("--error-type",   default="compilation",
                        choices=["compilation", "runtime"],
                        help="Type of error: 'compilation' or 'runtime' (default: compilation)")
    parser.add_argument("--error",        required=True,
                        help="The error message string returned by the test executor")
    parser.add_argument("--output",       default=None,
                        help="Write the prompt to this file instead of stdout")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    failed_test_src = Path(args.failed_test).read_text(encoding="utf-8")

    prompt = build_repair_prompt_for_target(
        target_file=args.file,
        function_name=args.func,
        target_line=args.start_line,
        project_root=args.project_root,
        failed_test=failed_test_src,
        error_message=args.error,
        error_type=args.error_type,
        end_line=args.end_line,
        unit_type=args.unit_type,
        tests_dir=args.tests_dir,
    )

    if args.output:
        Path(args.output).write_text(prompt, encoding="utf-8")
        print(f"[✓] Repair prompt written to: {args.output}")
    else:
        print(prompt)


if __name__ == "__main__":
    main()
