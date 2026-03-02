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
from typing import Dict, List, Optional, Set
from testtailor.models import ExecutionPath


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
