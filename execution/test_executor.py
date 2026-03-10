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
import argparse
from pathlib import Path
from typing import Optional, Set, Tuple, List

from models import CodeUnit, GeneratedTest


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
cov = coverage.Coverage(source=[os.path.dirname(target_file)], branch=False)
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

ns = {{
    "__file__": target_file,
    "__name__": "__main__",
    "__package__": None,
}}
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
                result.newly_covered_lines = set[int](data.get("newly_covered", []))
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

    cov = coverage_mod.Coverage(source=[os.path.dirname(target_file)], branch=True)
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


# ──────────────────────────────────────────────────────────────────────────────
# CLI entry point (manual verification)
# ──────────────────────────────────────────────────────────────────────────────

def _resolve_unit_from_function(
    target_file: str,
    function: str,
    unit_id: Optional[str] = None,
) -> CodeUnit:
    """
    Create a CodeUnit spanning a function definition inside *target_file*.

    Supported formats:
    - "func_name" (top-level function)
    - "ClassName.func_name" (method)
    """
    src = Path(target_file).read_text(encoding="utf-8")
    tree = ast.parse(src)

    class_name: Optional[str] = None
    func_name = function
    if "." in function:
        class_name, func_name = function.split(".", 1)

    node_found: Optional[ast.AST] = None
    if class_name:
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name == func_name:
                        node_found = item
                        break
    else:
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                node_found = node
                break

    if node_found is None or not isinstance(node_found, ast.FunctionDef):
        raise ValueError(f"Could not find function '{function}' in {target_file}")

    return CodeUnit(
        unit_id=unit_id or function,
        source_file=os.path.realpath(target_file),
        function_name=func_name,
        start_lineno=node_found.lineno,
        end_lineno=node_found.end_lineno,
        unit_type="linear",
        code_snippet="",
        ast_node=None,
    )


def _resolve_unit_from_lines(
    target_file: str,
    start: int,
    end: int,
    unit_id: str = "manual_unit",
) -> CodeUnit:
    return CodeUnit(
        unit_id=unit_id,
        source_file=os.path.realpath(target_file),
        function_name=unit_id,
        start_lineno=start,
        end_lineno=end,
        unit_type="linear",
        code_snippet="",
        ast_node=None,
    )


def main(argv: Optional[List[str]] = None) -> int:
    """
    Run a generated test against a target file and print results as JSON.

    Example (order_management):
      python -m execution.test_executor \\
        --target-file tests/order_management/service/order_service.py \\
        --function OrderService.create_order \\
        --test-file tests/test_test_executor_order_management.py
    """
    parser = argparse.ArgumentParser(description="Manual runner for TestExecutor.")
    parser.add_argument("--target-file", required=True, help="Path to Python file under test.")
    parser.add_argument(
        "--function",
        help="Function to define the unit (func or Class.func). Preferred over --unit-lines.",
    )
    parser.add_argument(
        "--unit-lines",
        nargs=2,
        type=int,
        metavar=("START", "END"),
        help="Manual unit line range (1-indexed), inclusive.",
    )
    parser.add_argument("--unit-id", default=None, help="Override CodeUnit.unit_id.")
    parser.add_argument("--test-file", help="Path to a Python file containing the generated test.")
    parser.add_argument(
        "--test-source",
        help="Inline test source string (if provided, overrides --test-file).",
    )
    parser.add_argument("--timeout", type=int, default=30, help="Subprocess timeout seconds.")
    parser.add_argument(
        "--baseline-covered",
        default="",
        help="Comma-separated covered line numbers for baseline diff (e.g., '10,11,12').",
    )
    parser.add_argument(
        "--also-measure-coverage",
        action="store_true",
        help="Additionally run measure_coverage on the provided test source.",
    )

    args = parser.parse_args(argv)

    target_file = os.path.realpath(args.target_file)
    if args.test_source is not None:
        test_source = textwrap.dedent(args.test_source)
    elif args.test_file:
        test_source = Path(args.test_file).read_text(encoding="utf-8")
    else:
        raise SystemExit("Must provide --test-source or --test-file")

    baseline: Set[int] = set()
    if args.baseline_covered.strip():
        baseline = {int(x.strip()) for x in args.baseline_covered.split(",") if x.strip()}

    if args.function:
        unit = _resolve_unit_from_function(target_file, args.function, unit_id=args.unit_id)
    elif args.unit_lines:
        unit = _resolve_unit_from_lines(
            target_file, start=args.unit_lines[0], end=args.unit_lines[1], unit_id=args.unit_id or "manual_unit"
        )
    else:
        raise SystemExit("Must provide --function or --unit-lines START END")

    executor = TestExecutor(target_file=target_file, timeout=args.timeout)
    result = executor.execute(
        generated_source=test_source,
        unit=unit,
        baseline_covered=baseline,
        iteration=0,
    )

    payload = {
        "unit_id": result.unit_id,
        "executed": result.executed,
        "compilation_error": result.compilation_error,
        "runtime_error": result.runtime_error,
        "newly_covered_lines": sorted(result.newly_covered_lines),
        "covers_target": result.covers_target,
        "reaches_function": result.reaches_function,
    }

    if args.also_measure_coverage:
        stmt_cov, br_cov = measure_coverage(target_file=target_file, test_suite_sources={"cli_test": test_source})
        payload["statement_coverage_pct"] = stmt_cov
        payload["branch_coverage_pct"] = br_cov

    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
