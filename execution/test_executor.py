"""
Test Executor
=============
Compiles and runs a generated test in an isolated subprocess, then measures
coverage using the `coverage` package.

Returns a GeneratedTest with:
  - compiled/executed status
  - error messages if any
  - newly covered lines
  - whether the target unit is fully covered
"""

import os
import sys
import ast
import subprocess
import tempfile
import textwrap
import json
from pathlib import Path
from typing import Optional, Set, Tuple

from testtailor.models import CodeUnit, GeneratedTest


# ──────────────────────────────────────────────────────────────────────────────
# Syntax check (fast, in-process)
# ──────────────────────────────────────────────────────────────────────────────

def _check_syntax(source: str) -> Optional[str]:
    """Return error string if source has a syntax error, else None."""
    try:
        ast.parse(source)
        return None
    except SyntaxError as e:
        return f"SyntaxError at line {e.lineno}: {e.msg}"


# ──────────────────────────────────────────────────────────────────────────────
# Test runner (subprocess-based for isolation)
# ──────────────────────────────────────────────────────────────────────────────

_RUNNER_SCRIPT = """\
import sys, json, coverage, traceback, unittest, importlib.util, os

target_file = {target_file!r}
test_source = {test_source!r}
unit_start  = {unit_start!r}
unit_end    = {unit_end!r}
baseline_lines = set({baseline_lines!r})

# Start coverage measurement
cov = coverage.Coverage(source=[target_file], branch=False)
cov.start()

result = {{
    "compiled": False,
    "executed": False,
    "compilation_error": None,
    "runtime_error": None,
    "newly_covered": [],
    "covers_target": False,
    "reaches_function": False,
}}

try:
    code = compile(test_source, "<generated_test>", "exec")
    result["compiled"] = True
except Exception as e:
    result["compilation_error"] = f"{{type(e).__name__}}: {{e}}"
    cov.stop()
    print(json.dumps(result))
    sys.exit(0)

ns = {{}}
try:
    exec(code, ns)
    # Run unittest test cases found in ns
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for name, obj in ns.items():
        if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
            suite.addTests(loader.loadTestsFromTestCase(obj))
    runner = unittest.TextTestRunner(stream=open(os.devnull, 'w'), verbosity=0)
    runner.run(suite)
    result["executed"] = True
except SystemExit:
    result["executed"] = True
except Exception as e:
    result["runtime_error"] = traceback.format_exc(limit=5)

cov.stop()
try:
    cov.save()
    data = cov.get_data()
    file_key = None
    for fn in data.measured_files():
        if os.path.realpath(fn) == os.path.realpath(target_file):
            file_key = fn
            break
    if file_key:
        covered = set(data.lines(file_key) or [])
        new_lines = sorted(covered - baseline_lines)
        result["newly_covered"] = new_lines
        target_lines = set(range(unit_start, unit_end + 1))
        result["covers_target"] = bool(target_lines.issubset(covered))
        result["reaches_function"] = bool(covered)
except Exception:
    pass

print(json.dumps(result))
"""


class TestExecutor:
    """
    Runs a generated test in a subprocess and returns evaluation results.
    """

    def __init__(self, target_file: str, timeout: int = 30):
        self.target_file = os.path.realpath(target_file)
        self.timeout = timeout

    def execute(
        self,
        generated_source: str,
        unit: CodeUnit,
        baseline_covered: Set[int],
        iteration: int = 0,
    ) -> GeneratedTest:
        """
        Execute *generated_source* and return a populated GeneratedTest.
        """
        result = GeneratedTest(
            unit_id=unit.unit_id,
            iteration=iteration,
            source=generated_source,
        )

        # Fast syntax check before spinning up subprocess
        syntax_err = _check_syntax(generated_source)
        if syntax_err:
            result.compilation_error = syntax_err
            return result

        # Build the runner script
        runner_code = _RUNNER_SCRIPT.format(
            target_file=self.target_file,
            test_source=generated_source,
            unit_start=unit.start_lineno,
            unit_end=unit.end_lineno,
            baseline_lines=sorted(baseline_covered),
        )

        # Write to a temp file and execute
        with tempfile.NamedTemporaryFile(
            suffix=".py", mode="w", delete=False, encoding="utf-8"
        ) as f:
            f.write(runner_code)
            runner_path = f.name

        try:
            proc = subprocess.run(
                [sys.executable, runner_path],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                env={**os.environ, "PYTHONPATH": str(Path(self.target_file).parent.parent)},
            )
            stdout = proc.stdout.strip()
            if stdout:
                data = json.loads(stdout)
                result.compilation_error = data.get("compilation_error")
                result.runtime_error = data.get("runtime_error")
                result.executed = data.get("executed", False)
                result.newly_covered_lines = set(data.get("newly_covered", []))
                result.covers_target = data.get("covers_target", False)
                result.reaches_function = data.get("reaches_function", False)
            else:
                result.runtime_error = (
                    f"Runner produced no output. stderr:\n{proc.stderr[:500]}"
                )
        except subprocess.TimeoutExpired:
            result.runtime_error = f"Test timed out after {self.timeout}s"
        except json.JSONDecodeError as e:
            result.runtime_error = f"Could not parse runner output: {e}"
        finally:
            Path(runner_path).unlink(missing_ok=True)

        return result


# ──────────────────────────────────────────────────────────────────────────────
# Coverage measurement (standalone, no test execution)
# ──────────────────────────────────────────────────────────────────────────────

def measure_coverage(
    target_file: str,
    test_suite_sources: dict,  # test_id → source
    timeout: int = 60,
) -> Tuple[float, float]:
    """
    Run all tests in *test_suite_sources* and measure statement & branch
    coverage of *target_file*.

    Returns (statement_coverage_pct, branch_coverage_pct).
    """
    try:
        import coverage as coverage_mod
    except ImportError:
        raise RuntimeError("coverage package required: pip install coverage")

    cov = coverage_mod.Coverage(source=[target_file], branch=True)
    cov.start()

    for test_id, source in test_suite_sources.items():
        try:
            code = compile(source, f"<{test_id}>", "exec")
            ns: dict = {}
            exec(code, ns)
            import unittest
            loader = unittest.TestLoader()
            suite = unittest.TestSuite()
            for name, obj in ns.items():
                if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                    suite.addTests(loader.loadTestsFromTestCase(obj))
            import io
            runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0)
            runner.run(suite)
        except Exception:
            pass

    cov.stop()

    try:
        cov.save()
        total_stmts, exec_stmts, total_br, exec_br = 0, 0, 0, 0
        data = cov.get_data()
        for fn in data.measured_files():
            if os.path.realpath(fn) == os.path.realpath(target_file):
                analysis = cov.analysis2(fn)
                _, stmts, excluded, missing, _ = analysis
                executed = set(stmts) - set(missing)
                total_stmts += len(stmts)
                exec_stmts += len(executed)

        stmt_cov = (exec_stmts / total_stmts * 100) if total_stmts else 0.0
        br_cov = 0.0  # branch analysis requires more setup; simplified here
        return stmt_cov, br_cov
    except Exception:
        return 0.0, 0.0
