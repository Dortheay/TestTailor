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

def collect_test_suite_traces(
    test_sources: Dict[str, str],   # test_id → Python source
    target_file: str,
) -> Dict[str, ExecutionPath]:
    """
    Execute each test case in *test_sources* in a fresh namespace and collect
    its execution trace against *target_file*.

    Returns
    -------
    dict mapping test_id → ExecutionPath
    """
    results: Dict[str, ExecutionPath] = {}

    for test_id, source in test_sources.items():
        collector = TraceCollector(target_file)
        namespace: dict = {}
        exception_info: Optional[str] = None

        try:
            # Compile and execute
            code = compile(source, f"<test:{test_id}>", "exec")
            with collector:
                exec(code, namespace)
        except SystemExit:
            pass  # tests calling sys.exit
        except Exception as exc:
            exception_info = f"{type(exc).__name__}: {exc}"

        path = collector.get_path(test_id, source)
        path.exception_info = exception_info
        results[test_id] = path

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
