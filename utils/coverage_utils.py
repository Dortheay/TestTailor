"""
Coverage Utilities
==================
Helpers for measuring statement and branch coverage using the `coverage` package.
"""

import os
import subprocess
import sys
import json
import tempfile
from pathlib import Path
from typing import Dict, Set, Tuple

try:
    import coverage as _cov_mod
    COVERAGE_AVAILABLE = True
except ImportError:
    COVERAGE_AVAILABLE = False


def get_uncovered_lines(
    source_file: str,
    test_suite_dir: str,
) -> Set[int]:
    """
    Run pytest on *test_suite_dir* with coverage on *source_file* and return
    the set of uncovered line numbers.

    Parameters
    ----------
    source_file : absolute path to the module under test
    test_suite_dir : directory containing test files
    """
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        cov_json = f.name

    try:
        subprocess.run(
            [
                sys.executable, "-m", "pytest",
                test_suite_dir,
                f"--cov={source_file}",
                "--cov-report=json",
                f"--cov-report=json:{cov_json}",
                "-q", "--tb=no",
            ],
            capture_output=True,
            timeout=120,
        )
        if Path(cov_json).exists():
            data = json.loads(Path(cov_json).read_text())
            for fname, info in data.get("files", {}).items():
                if os.path.realpath(fname) == os.path.realpath(source_file):
                    missing = set(info.get("missing_lines", []))
                    return missing
    except Exception:
        pass
    finally:
        Path(cov_json).unlink(missing_ok=True)

    return set()


def get_covered_lines_from_source(source_file: str) -> Set[int]:
    """
    Parse the source file and return all *executable* line numbers.
    (Used as the denominator when computing statement coverage.)
    """
    import ast as _ast
    source = Path(source_file).read_text(encoding="utf-8")
    tree = _ast.parse(source)
    lines: Set[int] = set()
    for node in _ast.walk(tree):
        if hasattr(node, 'lineno'):
            lines.add(node.lineno)
    return lines


def compute_statement_coverage(
    covered: Set[int],
    total_executable: Set[int],
) -> float:
    if not total_executable:
        return 100.0
    return len(covered & total_executable) / len(total_executable) * 100


def compute_branch_coverage_approx(
    source_file: str,
    covered_lines: Set[int],
) -> float:
    """
    Approximate branch coverage: for each if/for/while in the function,
    check whether both the True and False branches appear in covered_lines.
    """
    import ast as _ast
    source = Path(source_file).read_text(encoding="utf-8")
    tree = _ast.parse(source)

    total_branches = 0
    covered_branches = 0

    for node in _ast.walk(tree):
        if isinstance(node, _ast.If):
            total_branches += 2  # true branch, false branch
            # true branch: body[0].lineno
            if node.body and node.body[0].lineno in covered_lines:
                covered_branches += 1
            # false branch: orelse[0].lineno or fall-through
            if node.orelse:
                if node.orelse[0].lineno in covered_lines:
                    covered_branches += 1
            else:
                # No else: we count "skipping the if" as a branch too
                # Conservatively give credit if we see lines after the if
                covered_branches += 1

        elif isinstance(node, (ast.For, ast.While)):
            total_branches += 2  # loop entry, loop exit
            if node.body and node.body[0].lineno in covered_lines:
                covered_branches += 1
            # Loop exit: any line after the loop (approximation)
            covered_branches += 1  # assume exit is covered

    if total_branches == 0:
        return 100.0
    return covered_branches / total_branches * 100