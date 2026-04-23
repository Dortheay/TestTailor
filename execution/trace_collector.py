"""
Execution Trace Collector
==========================
Captures line-level execution traces for test cases using Python's built-in
`sys.settrace` facility.  Only events within the *target module* are retained,
yielding compact yet complete runtime paths.
"""

import sys
import os
import threading
import argparse
import json
import textwrap
from pathlib import Path
from typing import Dict, List, Optional, Set
from models import ExecutionPath
import unittest
import io


def _run_with_pytest(test_id: str, collector: "TraceCollector", target_file_abs: str):
    """
    Run a pytest-style test file (top-level test_* functions, fixtures from conftest)
    while the given TraceCollector is active. Works by registering a small pytest
    plugin that re-installs the collector's trace function around each test item.
    """
    try:
        import pytest
    except ImportError:
        print(f"    [!] pytest not installed, cannot run {test_id}")
        return

    if not (os.path.isfile(test_id) and test_id.endswith(".py")):
        print(f"    [!] pytest fallback needs a file path as test_id, got {test_id}")
        return

    trace_fn = collector._trace_calls

    class _TraceWrapPlugin:
        def pytest_runtest_call(self, item):
            sys.settrace(trace_fn)
            try:
                item.runtest()
            finally:
                sys.settrace(None)

        def pytest_runtest_protocol(self, item, nextitem):
            return None  # let default protocol run

    # Ensure conftest.py in the same dir is picked up automatically by pytest.
    argv = [
        test_id,
        "-p", "no:cacheprovider",
        "--tb=no",
        "-q",
        "--no-header",
        "-x",
        "--disable-warnings",
    ]
    try:
        # Temporarily drop settrace during pytest startup (collection/import);
        # the plugin re-enables it around each test call.
        sys.settrace(None)
        rc = pytest.main(argv, plugins=[_TraceWrapPlugin()])
        print(f"    [pytest] finished with exit code {rc}")
    except Exception as exc:
        print(f"    [pytest] crashed: {type(exc).__name__}: {exc}")
    finally:
        sys.settrace(trace_fn)


# ──────────────────────────────────────────────────────────────────────────────
# Trace collector
# ──────────────────────────────────────────────────────────────────────────────

class TraceCollector:
    """
    A sys.settrace-based collector.

    Usage
    -----
    collector = TraceCollector(target_module_path)
    with collector:
        exec(test_code)
    path = collector.get_path("my_test")
    """

    def __init__(self, target_file: str):
        # Normalise so we can compare with frame.f_code.co_filename
        self.target_file = os.path.realpath(target_file)
        self._visited_lines: List[int] = []
        self._covered: Set[int] = set()
        self._active = False

    # ── Context manager ──────────────────────────────────────────────────────

    def __enter__(self):
        self._visited_lines = []
        self._covered = set()
        self._active = True
        sys.settrace(self._trace_calls)
        threading.settrace(self._trace_calls)
        return self

    def __exit__(self, *_):
        sys.settrace(None)
        threading.settrace(None)
        self._active = False

    # ── Trace handler ────────────────────────────────────────────────────────

    def _trace_calls(self, frame, event, arg):
        """Called by Python interpreter for every call / line / return event."""
        filename = os.path.realpath(frame.f_code.co_filename)
        if filename != self.target_file:
            return None  # don't trace other modules
        if event in ('call', 'line', 'return'):
            lineno = frame.f_lineno
            self._visited_lines.append(lineno)
            self._covered.add(lineno)
        return self._trace_calls  # return self to keep tracing inside this frame

    # ── Result access ────────────────────────────────────────────────────────

    def get_path(self, test_id: str, test_source: str = "") -> ExecutionPath:
        return ExecutionPath(
            test_id=test_id,
            test_source=test_source,
            covered_lines=set(self._covered),
            visited_nodes=list(self._visited_lines),
        )

    @property
    def covered_lines(self) -> Set[int]:
        return set(self._covered)

    @property
    def visited_order(self) -> List[int]:
        return list(self._visited_lines)


# ──────────────────────────────────────────────────────────────────────────────
# Collect traces for an existing test suite
# ──────────────────────────────────────────────────────────────────────────────

# trace_collector.py

def collect_test_suite_traces(
    test_sources: Dict[str, str],   # test_id → Python source
    target_file: str,
) -> Dict[str, ExecutionPath]:
    results: Dict[str, ExecutionPath] = {}
    target_file_abs = os.path.realpath(target_file)
    original_argv = sys.argv[:]

    print(f"\n{'='*20} Trace Collection Start {'='*20}")

    for test_id, source in test_sources.items():
        print(f"\n[Test Case: {test_id}]")
        collector = TraceCollector(target_file_abs)
        
        namespace: dict = {
            "__file__": target_file_abs,
            "__name__": "__main__",
        }
        sys.argv = [original_argv[0], "-v"] 

        try:
            code = compile(source, f"<test:{test_id}>", "exec")
            with collector:
                # Step 1: Execute code to define classes, separately catch SystemExit
                try:
                    exec(code, namespace)
                except SystemExit:
                    pass  # Ignore exit triggered by unittest.main(), continue execution
                except Exception as exc:
                    print(f"    [ERROR] Execution crashed: {type(exc).__name__}: {exc}")

                # Step 2: Manually load and run tests (this will always execute)
                loader = unittest.TestLoader()
                suite = unittest.TestSuite()
                for obj in namespace.values():
                    if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                        suite.addTests(loader.loadTestsFromTestCase(obj))
                
                if suite.countTestCases() > 0:
                    runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0)
                    runner.run(suite)
                else:
                    # Fallback: pytest-style file (top-level test_* functions / fixtures)
                    print(f"    [*] No unittest.TestCase found; falling back to pytest runner")
                    _run_with_pytest(test_id, collector, target_file_abs)

        except SystemExit:
            pass 
        except Exception as exc:
            print(f"    [ERROR] Execution crashed: {type(exc).__name__}: {exc}")

        # 4. Retrieve the result and print the specific covered line numbers
        path = collector.get_path(test_id, source)
        results[test_id] = path
        
        covered_list = sorted(list(path.covered_lines))
        print(f"    [SUCCESS] Covered lines count: {len(covered_list)}")
        print(f"    [SUCCESS] Covered line numbers: {covered_list}")

    sys.argv = original_argv
    print(f"\n{'='*20} Trace Collection End {'='*20}\n")
    return results
# ──────────────────────────────────────────────────────────────────────────────
# CLI entry point (manual verification)
# ──────────────────────────────────────────────────────────────────────────────

def main(argv: Optional[List[str]] = None) -> int:
    """
    Simple CLI for manually exercising the trace collector.

    Example (order_management):
      python -m execution.trace_collector \\
        --target-file tests/order_management/service/order_service.py \\
        --test-file tests/_cli_trace_order_test.py
    """
    parser = argparse.ArgumentParser(description="Manual runner for TraceCollector.")
    parser.add_argument(
        "--target-file",
        required=True,
        help="Path to the Python file whose execution we want to trace.",
    )
    parser.add_argument(
        "--test-file",
        help="Path to a Python file containing a unittest-style test.",
    )
    parser.add_argument(
        "--test-source",
        help="Inline test source string (if provided, overrides --test-file).",
    )
    parser.add_argument(
        "--test-id",
        default="cli_test",
        help="Identifier used as test_id key in the result JSON.",
    )

    args = parser.parse_args(argv)

    if args.test_source is not None:
        test_src = textwrap.dedent(args.test_source)
    elif args.test_file:
        test_src = Path(args.test_file).read_text(encoding="utf-8")
    else:
        raise SystemExit("Must provide --test-source or --test-file")

    test_sources = {args.test_id: test_src}
    traces = collect_test_suite_traces(
        test_sources=test_sources,
        target_file=os.path.realpath(args.target_file),
    )

    # Convert ExecutionPath objects to a JSON-serialisable structure.
    out: Dict[str, Dict[str, object]] = {}
    for test_id, path in traces.items():
        out[test_id] = {
            "covered_lines": sorted(path.covered_lines),
            "visited_nodes": path.visited_nodes,
            "reached_function": bool(path.covered_lines),
            "exception_info": path.exception_info,
        }

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
