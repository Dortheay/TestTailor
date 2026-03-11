"""
Unit tests for path_analysis.path_divergence
=============================================

Coverage
--------
- PathDivergenceAnalyzer._find_divergence
- PathDivergenceAnalyzer._get_condition_at_line
- PathDivergenceAnalyzer._what_target_does_next
- PathDivergenceAnalyzer._what_proximal_does_next
- PathDivergenceAnalyzer.analyze  (integration)
- format_divergence
- analyze_divergence  (high-level entry point)
"""

import os
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models import CodeUnit, ExecutionPath, PathConstraint, PathProximalTest, TargetPath
from path_analysis.path_divergence import (
    PathDivergenceAnalyzer,
    analyze_divergence,
    format_divergence,
)


# ──────────────────────────────────────────────────────────────────────────────
# Embedded source fixtures
# ──────────────────────────────────────────────────────────────────────────────

# Simple if-else function
# line 1: def simple(x):
# line 2:     if x > 0:
# line 3:         return x
# line 4:     else:            ← no AST node; raw line = "else:"
# line 5:         return -x
SIMPLE_SOURCE = textwrap.dedent("""\
    def simple(x):
        if x > 0:
            return x
        else:
            return -x
""")

# For-loop + while-loop function
# line 1: def loop_func(n):
# line 2:     total = 0
# line 3:     for i in range(n):
# line 4:         total += i
# line 5:     while total < 100:
# line 6:         total += 10
# line 7:     return total
LOOP_SOURCE = textwrap.dedent("""\
    def loop_func(n):
        total = 0
        for i in range(n):
            total += i
        while total < 100:
            total += 10
        return total
""")

# Try/except function
# line 1: def with_try(x):
# line 2:     try:
# line 3:         if x > 0:
# line 4:             return x
# line 5:         return 0
# line 6:     except ValueError:
# line 7:         return -1
WITH_TRY_SOURCE = textwrap.dedent("""\
    def with_try(x):
        try:
            if x > 0:
                return x
            return 0
        except ValueError:
            return -1
""")

# Class with a method
# line 1: class MyClass:
# line 2:     def method(self, v):
# line 3:         return v * 2
CLASS_SOURCE = textwrap.dedent("""\
    class MyClass:
        def method(self, v):
            return v * 2
""")

# Nested-branch function (deeper divergence scenarios)
# line 1: def nested(a, b):
# line 2:     if a > 0:
# line 3:         if b > 0:
# line 4:             return "both positive"
# line 5:         else:
# line 6:             return "a positive b not"
# line 7:     else:
# line 8:         return "a not positive"
NESTED_SOURCE = textwrap.dedent("""\
    def nested(a, b):
        if a > 0:
            if b > 0:
                return "both positive"
            else:
                return "a positive b not"
        else:
            return "a not positive"
""")


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _unit(
    function_name: str,
    start: int,
    end: int = 0,
    source_file: str = "",
    unit_id: str = "u",
) -> CodeUnit:
    return CodeUnit(
        unit_id=unit_id,
        source_file=source_file,
        function_name=function_name,
        start_lineno=start,
        end_lineno=end or start,
        unit_type="linear",
        code_snippet="",
    )


def _exec_path(test_id: str, visited: list) -> ExecutionPath:
    return ExecutionPath(
        test_id=test_id,
        test_source="",
        covered_lines=set(visited),
        visited_nodes=list(visited),
    )


def _proximal(test_id: str, visited: list, score: float = 0.5) -> PathProximalTest:
    return PathProximalTest(
        test_id=test_id,
        test_source="",
        execution_path=_exec_path(test_id, visited),
        jaccard_similarity=score,
    )


def _target_path(unit: CodeUnit, path_nodes: list) -> TargetPath:
    return TargetPath(unit=unit, constraints=[], path_nodes=path_nodes)


def _write_tempfile(source: str) -> str:
    """Write *source* to a temporary .py file and return its real path."""
    f = tempfile.NamedTemporaryFile(
        suffix=".py", mode="w", delete=False, encoding="utf-8"
    )
    f.write(source)
    f.flush()
    f.close()
    return os.path.realpath(f.name)


# ──────────────────────────────────────────────────────────────────────────────
# Tests: _find_divergence
# ──────────────────────────────────────────────────────────────────────────────

class TestFindDivergence(unittest.TestCase):
    """Unit tests for PathDivergenceAnalyzer._find_divergence."""

    def setUp(self):
        self.analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)

    # ── basic cases ───────────────────────────────────────────────────────────

    def test_branch_not_taken_returns_first_missing_node(self):
        """Proximal test takes the True branch; else body (line 5) is divergence."""
        # target: func-entry(1) → if-condition(2) → else-body(5)
        # proximal: covers lines 1, 2, 3 (True branch)
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[1, 2, 5],
            proximal_seq=[1, 2, 3],
        )
        self.assertEqual(div, 5)
        self.assertIsNotNone(cond)
        self.assertEqual(last, 2)  # line 2 is the last shared node

    def test_no_divergence_when_all_target_nodes_covered(self):
        """All target path nodes are covered → no divergence."""
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[1, 2, 5],
            proximal_seq=[1, 2, 5],
        )
        self.assertIsNone(div)
        self.assertIsNone(cond)
        self.assertEqual(last, 5)  # all covered; last_shared = final target node

    def test_divergence_when_no_shared_nodes(self):
        """Proximal covers completely different lines → diverges at the very first target node."""
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[1, 2, 5],
            proximal_seq=[3],
        )
        self.assertEqual(div, 1)
        self.assertIsNone(last)

    def test_divergence_at_first_node_none_last_shared(self):
        """If the very first target node is not covered, last_shared is None."""
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[2, 5],
            proximal_seq=[1, 3],  # has 1, 3 but not 2
        )
        self.assertEqual(div, 2)
        self.assertIsNone(last)

    def test_empty_target_seq_returns_all_none(self):
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[],
            proximal_seq=[1, 2, 3],
        )
        self.assertIsNone(div)
        self.assertIsNone(cond)
        self.assertIsNone(last)

    def test_empty_proximal_seq_diverges_at_first_target(self):
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[1, 2, 5],
            proximal_seq=[],
        )
        self.assertEqual(div, 1)
        self.assertIsNone(last)

    def test_both_empty_sequences_returns_all_none(self):
        div, cond, last = self.analyzer._find_divergence([], [])
        self.assertIsNone(div)
        self.assertIsNone(cond)
        self.assertIsNone(last)

    # ── ordering: set membership, not positional ──────────────────────────────

    def test_uses_set_membership_not_position(self):
        """Even if proximal_seq contains a target node out of order, it still counts."""
        # target: [1, 2, 5]  — proximal covers {5, 3} (has line 5 but not 1, 2)
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[1, 2, 5],
            proximal_seq=[5, 3],
        )
        self.assertEqual(div, 1)   # line 1 is first target node missing
        self.assertIsNone(last)

    def test_last_shared_correctly_tracks_last_covered_target_node(self):
        """last_shared should be the last sequential match, not just any match."""
        # target: [1, 2, 5]  — proximal covers {1, 5} but not 2
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[1, 2, 5],
            proximal_seq=[1, 5],
        )
        self.assertEqual(div, 2)   # line 2 is the first uncovered
        self.assertEqual(last, 1)  # last covered before divergence

    # ── loop scenario ─────────────────────────────────────────────────────────

    def test_loop_proximal_skips_while_body(self):
        """
        Loop scenario using LOOP_SOURCE.
        Target path: [1, 3, 5, 6] (for + while).
        Proximal: runs for-loop twice then returns, skipping while-loop body.
        """
        analyzer = PathDivergenceAnalyzer(LOOP_SOURCE)
        # proximal visits: func-entry(1), total=0(2), for-header(3), body(4),
        #                  for-header again(3), body again(4), for-header(3),
        #                  return(7)
        div, cond, last = analyzer._find_divergence(
            target_seq=[1, 3, 5, 6],
            proximal_seq=[1, 2, 3, 4, 3, 4, 3, 7],
        )
        self.assertEqual(div, 5)    # while-header not visited
        self.assertEqual(last, 3)   # last shared target node was for-header

    def test_loop_line_visited_multiple_times_still_counts_as_covered(self):
        """A line visited ≥1 time in proximal trace is treated as covered."""
        analyzer = PathDivergenceAnalyzer(LOOP_SOURCE)
        # Even with repeats, line 3 and 5 are both covered
        div, cond, last = analyzer._find_divergence(
            target_seq=[1, 3, 5],
            proximal_seq=[1, 3, 4, 3, 5, 6, 5, 7],
        )
        self.assertIsNone(div)  # all target nodes covered
        self.assertEqual(last, 5)

    # ── condition text ────────────────────────────────────────────────────────

    def test_condition_text_is_not_empty_on_divergence(self):
        div, cond, last = self.analyzer._find_divergence(
            target_seq=[1, 2, 5],
            proximal_seq=[1, 2, 3],
        )
        self.assertIsNotNone(cond)
        self.assertGreater(len(cond), 0)


# ──────────────────────────────────────────────────────────────────────────────
# Tests: _get_condition_at_line
# ──────────────────────────────────────────────────────────────────────────────

class TestGetConditionAtLine(unittest.TestCase):
    """Unit tests for PathDivergenceAnalyzer._get_condition_at_line."""

    # ── SIMPLE_SOURCE ─────────────────────────────────────────────────────────

    def setUp(self):
        self.simple = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        self.loop   = PathDivergenceAnalyzer(LOOP_SOURCE)
        self.try_   = PathDivergenceAnalyzer(WITH_TRY_SOURCE)
        self.cls    = PathDivergenceAnalyzer(CLASS_SOURCE)

    def test_function_def_shows_signature_only(self):
        """FunctionDef → 'def func(args):' without function body."""
        result = self.simple._get_condition_at_line(1)
        self.assertEqual(result, "def simple(x):")
        self.assertNotIn("if", result)       # body must not appear
        self.assertNotIn("return", result)

    def test_if_condition_shows_predicate_only(self):
        """If node → 'if <test>' without body statements."""
        result = self.simple._get_condition_at_line(2)
        self.assertEqual(result, "if x > 0")
        self.assertNotIn("return", result)   # body must not appear

    def test_return_statement_in_true_branch(self):
        result = self.simple._get_condition_at_line(3)
        self.assertEqual(result, "return x")

    def test_return_unary_in_else_branch(self):
        result = self.simple._get_condition_at_line(5)
        self.assertEqual(result, "return -x")

    def test_else_keyword_line_falls_back_to_raw_source(self):
        """Line 4 ('    else:') has no AST node → raw source fallback."""
        result = self.simple._get_condition_at_line(4)
        self.assertIn("else", result)

    # ── LOOP_SOURCE ───────────────────────────────────────────────────────────

    def test_for_loop_shows_header_only(self):
        """For node → 'for <target> in <iter>' without body."""
        result = self.loop._get_condition_at_line(3)
        self.assertIn("for", result)
        self.assertIn("range(n)", result)
        self.assertNotIn("total", result)   # body must not appear

    def test_while_loop_shows_predicate_only(self):
        """While node → 'while <test>' without body."""
        result = self.loop._get_condition_at_line(5)
        self.assertEqual(result, "while total < 100")

    def test_simple_statement_augmented_assign(self):
        result = self.loop._get_condition_at_line(4)
        self.assertEqual(result, "total += i")

    def test_return_statement(self):
        result = self.loop._get_condition_at_line(7)
        self.assertEqual(result, "return total")

    # ── WITH_TRY_SOURCE ───────────────────────────────────────────────────────

    def test_try_block_shows_placeholder(self):
        """Try node → 'try: ...' without expanded body."""
        result = self.try_._get_condition_at_line(2)
        self.assertEqual(result, "try: ...")

    def test_nested_if_inside_try(self):
        result = self.try_._get_condition_at_line(3)
        self.assertEqual(result, "if x > 0")

    # ── CLASS_SOURCE ──────────────────────────────────────────────────────────

    def test_class_def_shows_name_only(self):
        """ClassDef → 'class Name:' without methods."""
        result = self.cls._get_condition_at_line(1)
        self.assertEqual(result, "class MyClass:")

    def test_method_inside_class(self):
        result = self.cls._get_condition_at_line(2)
        self.assertEqual(result, "def method(self, v):")

    # ── out-of-range / unknown lines ──────────────────────────────────────────

    def test_line_zero_returns_fallback_label(self):
        result = self.simple._get_condition_at_line(0)
        self.assertIn("0", result)

    def test_very_large_line_returns_fallback_label(self):
        result = self.simple._get_condition_at_line(9999)
        self.assertIn("9999", result)

    # ── CFG prefix ───────────────────────────────────────────────────────────

    def test_branch_prefix_when_cfg_loaded(self):
        """When CFG marks a line as 'branch', prefix '[branch] ' is prepended."""
        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        analyzer._lineno_to_node_type[2] = "branch"
        result = analyzer._get_condition_at_line(2)
        self.assertTrue(result.startswith("[branch] "))
        self.assertIn("x > 0", result)

    def test_loop_prefix_when_cfg_loaded(self):
        """When CFG marks a line as 'loop_header', prefix '[loop] ' is prepended."""
        analyzer = PathDivergenceAnalyzer(LOOP_SOURCE)
        analyzer._lineno_to_node_type[3] = "loop_header"
        result = analyzer._get_condition_at_line(3)
        self.assertTrue(result.startswith("[loop] "))
        self.assertIn("range(n)", result)

    def test_no_prefix_for_plain_statement(self):
        """Statement nodes without a CFG type annotation get no prefix."""
        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        result = analyzer._get_condition_at_line(3)
        self.assertFalse(result.startswith("["))


# ──────────────────────────────────────────────────────────────────────────────
# Tests: _what_target_does_next
# ──────────────────────────────────────────────────────────────────────────────

class TestWhatTargetDoesNext(unittest.TestCase):
    """Unit tests for PathDivergenceAnalyzer._what_target_does_next."""

    def setUp(self):
        self.analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)

    def test_returns_next_node_condition(self):
        """When a successor exists, return its condition text."""
        result = self.analyzer._what_target_does_next(
            target_seq=[1, 2, 5],
            after_lineno=2,
        )
        # Next node after line 2 is line 5 → "return -x"
        self.assertEqual(result, "return -x")

    def test_returns_fallback_when_after_is_last_in_seq(self):
        """When the divergence point is the last target node, no successor exists."""
        result = self.analyzer._what_target_does_next(
            target_seq=[1, 2, 5],
            after_lineno=5,
        )
        self.assertEqual(result, "(continues toward target unit)")

    def test_returns_fallback_when_lineno_not_in_seq(self):
        """If after_lineno is not in target_seq at all, return fallback."""
        result = self.analyzer._what_target_does_next(
            target_seq=[1, 2],
            after_lineno=99,
        )
        self.assertEqual(result, "(continues toward target unit)")

    def test_first_element_has_valid_successor(self):
        result = self.analyzer._what_target_does_next(
            target_seq=[1, 2, 5],
            after_lineno=1,
        )
        # successor of line 1 is line 2 → "if x > 0"
        self.assertEqual(result, "if x > 0")

    def test_single_element_seq_returns_fallback(self):
        result = self.analyzer._what_target_does_next(
            target_seq=[2],
            after_lineno=2,
        )
        self.assertEqual(result, "(continues toward target unit)")


# ──────────────────────────────────────────────────────────────────────────────
# Tests: _what_proximal_does_next
# ──────────────────────────────────────────────────────────────────────────────

class TestWhatProximalDoesNext(unittest.TestCase):
    """Unit tests for PathDivergenceAnalyzer._what_proximal_does_next."""

    def setUp(self):
        self.analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)

    # ── after_lineno is None ──────────────────────────────────────────────────

    def test_none_after_with_nonempty_trace_returns_first_line(self):
        """If no shared node, return the condition of the first line in trace."""
        result = self.analyzer._what_proximal_does_next(
            proximal_seq=[2, 3],
            after_lineno=None,
        )
        # First line is 2 → "if x > 0"
        self.assertEqual(result, "if x > 0")

    def test_none_after_with_empty_trace_returns_fallback(self):
        result = self.analyzer._what_proximal_does_next(
            proximal_seq=[],
            after_lineno=None,
        )
        self.assertEqual(result, "(different branch or skips entirely)")

    # ── normal cases ──────────────────────────────────────────────────────────

    def test_returns_line_immediately_after_shared_node(self):
        """After line 2 (last shared), proximal goes to line 3."""
        result = self.analyzer._what_proximal_does_next(
            proximal_seq=[1, 2, 3],
            after_lineno=2,
        )
        self.assertEqual(result, "return x")

    def test_after_last_line_in_trace_returns_fallback(self):
        """after_lineno is the final element of proximal_seq → no successor."""
        result = self.analyzer._what_proximal_does_next(
            proximal_seq=[1, 2, 3],
            after_lineno=3,
        )
        self.assertEqual(result, "(different branch or skips entirely)")

    def test_after_lineno_not_in_trace_returns_fallback(self):
        """after_lineno absent from proximal_seq → fallback."""
        result = self.analyzer._what_proximal_does_next(
            proximal_seq=[1, 2, 3],
            after_lineno=99,
        )
        self.assertEqual(result, "(different branch or skips entirely)")

    # ── loop: use last occurrence ─────────────────────────────────────────────

    def test_loop_uses_last_occurrence_of_shared_line(self):
        """
        When a line appears multiple times (loop), the last occurrence
        is used so that we correctly identify what comes *after* the loop.

        proximal_seq = [1, 2, 3, 4, 3, 4, 3, 7]
        Line 3 appears at indices 1, 3, 5.  Last occurrence is index 5.
        Next element is index 6 → line 7 → "return total".
        """
        analyzer = PathDivergenceAnalyzer(LOOP_SOURCE)
        result = analyzer._what_proximal_does_next(
            proximal_seq=[1, 2, 3, 4, 3, 4, 3, 7],
            after_lineno=3,
        )
        self.assertEqual(result, "return total")

    def test_loop_first_occurrence_would_give_wrong_answer(self):
        """
        Sanity check: if we had naively used the FIRST occurrence of line 3
        (index 1), the successor would be line 4, not 7.
        This test verifies we don't make that mistake.
        """
        analyzer = PathDivergenceAnalyzer(LOOP_SOURCE)
        result = analyzer._what_proximal_does_next(
            proximal_seq=[1, 2, 3, 4, 3, 4, 3, 7],
            after_lineno=3,
        )
        # Must NOT be line 4 (the loop body — which would be the first-occurrence answer)
        self.assertNotEqual(result, "total += i")

    def test_loop_intermediate_occurrence_not_used(self):
        """
        proximal_seq = [3, 4, 3, 5, 3, 7]
        Line 3 at indices 0, 2, 4.  Last → index 4.  Successor → line 7.
        """
        analyzer = PathDivergenceAnalyzer(LOOP_SOURCE)
        result = analyzer._what_proximal_does_next(
            proximal_seq=[3, 4, 3, 5, 3, 7],
            after_lineno=3,
        )
        self.assertEqual(result, "return total")


# ──────────────────────────────────────────────────────────────────────────────
# Tests: analyze  (integration)
# ──────────────────────────────────────────────────────────────────────────────

class TestAnalyze(unittest.TestCase):
    """Integration tests for PathDivergenceAnalyzer.analyze."""

    # ── simple if-else divergence ─────────────────────────────────────────────

    def test_else_branch_not_taken(self):
        """
        Target: reach line 5 (else body) via path [1, 2, 5].
        Proximal: took True branch, covered [1, 2, 3].

        Expected:
          divergence_lineno    = 5
          divergence_condition = "return -x"
          target_continues_to  = "(continues toward target unit)"  (line 5 is last in seq)
          proximal_continues   = "return x"  (after last shared node 2, proximal goes to 3)
        """
        unit = _unit("simple", start=5, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2, 5])
        p    = _proximal("test_a", visited=[1, 2, 3])

        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        result = analyzer.analyze(p, tp)

        self.assertEqual(result.divergence_lineno, 5)
        self.assertEqual(result.divergence_condition, "return -x")
        self.assertEqual(result.target_continues_to, "(continues toward target unit)")
        self.assertEqual(result.proximal_continues_to, "return x")

    def test_true_branch_not_taken(self):
        """
        Target: reach line 3 (true body) via path [1, 2, 3].
        Proximal: took False branch, covered [1, 2, 5].

        Expected:
          divergence_lineno    = 3
          divergence_condition = "return x"
          target_continues_to  = "(continues toward target unit)"
          proximal_continues   = "return -x"
        """
        unit = _unit("simple", start=3, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2, 3])
        p    = _proximal("test_b", visited=[1, 2, 5])

        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        result = analyzer.analyze(p, tp)

        self.assertEqual(result.divergence_lineno, 3)
        self.assertEqual(result.divergence_condition, "return x")
        self.assertEqual(result.proximal_continues_to, "return -x")

    def test_divergence_at_entry(self):
        """
        Proximal does not enter the function at all.
        Target path: [1, 2, 5].  Proximal: [].

        Expected: divergence at line 1 (function entry), last_shared = None.
        """
        unit = _unit("simple", start=5, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2, 5])
        p    = _proximal("test_c", visited=[])

        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        result = analyzer.analyze(p, tp)

        self.assertEqual(result.divergence_lineno, 1)
        self.assertIn("simple", result.divergence_condition)
        # proximal trace is empty → no specific next line
        self.assertEqual(result.proximal_continues_to, "(different branch or skips entirely)")

    # ── no divergence ─────────────────────────────────────────────────────────

    def test_no_divergence_populates_fallback_fields(self):
        """
        When all target path nodes are covered, use the fallback messages.
        """
        unit = _unit("simple", start=5, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2])
        p    = _proximal("test_d", visited=[1, 2, 5])

        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        result = analyzer.analyze(p, tp)

        self.assertIsNone(result.divergence_lineno)
        self.assertEqual(result.divergence_condition, "(could not pinpoint divergence)")
        self.assertIn("5", result.target_continues_to)   # unit.start_lineno=5
        self.assertEqual(result.proximal_continues_to, "(test did not reach this line)")

    # ── nested branches ───────────────────────────────────────────────────────

    def test_nested_branch_inner_divergence(self):
        """
        NESTED_SOURCE: target = 'both positive' at line 4.
        Path: [1, 2, 3, 4].
        Proximal: covers [1, 2, 6] → enters a>0 branch but takes b<=0 sub-branch.
        Divergence at line 3 (inner if).
        """
        unit = _unit("nested", start=4, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2, 3, 4])
        p    = _proximal("test_e", visited=[1, 2, 6])

        analyzer = PathDivergenceAnalyzer(NESTED_SOURCE)
        result = analyzer.analyze(p, tp)

        self.assertEqual(result.divergence_lineno, 3)
        self.assertIn("b > 0", result.divergence_condition)
        self.assertEqual(result.target_continues_to, "return 'both positive'")

    # ── loop divergence ───────────────────────────────────────────────────────

    def test_loop_while_not_entered(self):
        """
        LOOP_SOURCE: target = while body (line 6) via path [1, 3, 5, 6].
        Proximal visits for-loop but not while-loop.
        Divergence at line 5 (while header).
        """
        unit = _unit("loop_func", start=6, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 3, 5, 6])
        p    = _proximal("test_f", visited=[1, 2, 3, 4, 7])

        analyzer = PathDivergenceAnalyzer(LOOP_SOURCE)
        result = analyzer.analyze(p, tp)

        self.assertEqual(result.divergence_lineno, 5)
        self.assertIn("total < 100", result.divergence_condition)
        # proximal continues from last shared (3) → goes to 4
        self.assertEqual(result.proximal_continues_to, "total += i")

    # ── CFG enrichment ────────────────────────────────────────────────────────

    def test_cfg_prefix_applied_when_source_file_set(self):
        """
        When unit.source_file points to a real file and load_cfg succeeds,
        branch nodes should receive the '[branch] ' prefix.
        """
        tmp = _write_tempfile(SIMPLE_SOURCE)
        try:
            unit = _unit("simple", start=5, source_file=tmp, unit_id="u")
            tp   = _target_path(unit, path_nodes=[1, 2, 5])
            p    = _proximal("test_g", visited=[1, 2, 3])

            analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
            result = analyzer.analyze(p, tp)

            # Line 2 is marked as 'branch' by the CFG; line 5 is the divergence.
            # The condition at line 5 ('return -x') is a statement node, not a branch,
            # so it gets no prefix.
            self.assertEqual(result.divergence_lineno, 5)
            self.assertEqual(result.divergence_condition, "return -x")
        finally:
            os.unlink(tmp)

    def test_invalid_source_file_does_not_crash(self):
        """A non-existent source_file silently skips CFG loading."""
        unit = _unit("simple", start=5, source_file="/no/such/file.py")
        tp   = _target_path(unit, path_nodes=[1, 2, 5])
        p    = _proximal("test_h", visited=[1, 2, 3])

        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        # Should not raise
        result = analyzer.analyze(p, tp)
        self.assertEqual(result.divergence_lineno, 5)

    # ── return value ──────────────────────────────────────────────────────────

    def test_analyze_returns_same_proximal_object(self):
        """analyze() must return the same PathProximalTest instance (mutates in place)."""
        unit = _unit("simple", start=5, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2, 5])
        p    = _proximal("test_i", visited=[1, 2, 3])

        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        returned = analyzer.analyze(p, tp)
        self.assertIs(returned, p)


# ──────────────────────────────────────────────────────────────────────────────
# Tests: format_divergence
# ──────────────────────────────────────────────────────────────────────────────

class TestFormatDivergence(unittest.TestCase):
    """Unit tests for format_divergence()."""

    def _make_proximal_with_divergence(
        self,
        lineno=9,
        condition="if x > 0",
        target_cont="return x",
        proximal_cont="return -x",
    ) -> PathProximalTest:
        p = PathProximalTest(
            test_id="t",
            test_source="",
            execution_path=_exec_path("t", []),
            jaccard_similarity=0.8,
        )
        p.divergence_lineno = lineno
        p.divergence_condition = condition
        p.target_continues_to = target_cont
        p.proximal_continues_to = proximal_cont
        return p

    def test_output_contains_divergence_line_number(self):
        p = self._make_proximal_with_divergence(lineno=9)
        out = format_divergence(p)
        self.assertIn("9", out)

    def test_output_contains_divergence_condition(self):
        p = self._make_proximal_with_divergence(condition="if x > 0")
        out = format_divergence(p)
        self.assertIn("if x > 0", out)

    def test_output_contains_target_continues_to(self):
        p = self._make_proximal_with_divergence(target_cont="return x")
        out = format_divergence(p)
        self.assertIn("return x", out)

    def test_output_contains_proximal_continues_to(self):
        p = self._make_proximal_with_divergence(proximal_cont="return -x")
        out = format_divergence(p)
        self.assertIn("return -x", out)

    def test_output_has_section_headers(self):
        p = self._make_proximal_with_divergence()
        out = format_divergence(p)
        self.assertIn("Path Divergence Analysis", out)
        self.assertIn("Target path continues to", out)
        self.assertIn("Existing test path continues to", out)

    def test_no_lineno_divergence_omits_line_number_part(self):
        """When divergence_lineno is None/0 (no structural divergence found),
        the line number must not be appended."""
        p = PathProximalTest(
            test_id="t",
            test_source="",
            execution_path=_exec_path("t", []),
            jaccard_similarity=0.0,
        )
        p.divergence_lineno = None
        p.divergence_condition = "(could not pinpoint divergence)"
        p.target_continues_to = "line 5 (target unit)"
        p.proximal_continues_to = "(test did not reach this line)"

        out = format_divergence(p)
        self.assertIn("could not pinpoint divergence", out)
        # Should not contain "line None" or similar artefact
        self.assertNotIn("None", out)

    def test_output_is_multiline_string(self):
        p = self._make_proximal_with_divergence()
        out = format_divergence(p)
        self.assertGreater(out.count("\n"), 2)


# ──────────────────────────────────────────────────────────────────────────────
# Tests: analyze_divergence  (high-level entry point)
# ──────────────────────────────────────────────────────────────────────────────

class TestAnalyzeDivergenceEntryPoint(unittest.TestCase):
    """Tests for the module-level analyze_divergence() convenience function."""

    def test_delegates_to_analyzer_and_populates_fields(self):
        """analyze_divergence() must produce the same result as calling the
        class directly with the same arguments."""
        unit = _unit("simple", start=5, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2, 5])
        p1   = _proximal("t1", visited=[1, 2, 3])
        p2   = _proximal("t2", visited=[1, 2, 3])

        # Via the entry point
        result_entry = analyze_divergence(p1, tp, SIMPLE_SOURCE)

        # Via the class directly
        analyzer = PathDivergenceAnalyzer(SIMPLE_SOURCE)
        result_direct = analyzer.analyze(p2, tp)

        self.assertEqual(result_entry.divergence_lineno, result_direct.divergence_lineno)
        self.assertEqual(result_entry.divergence_condition, result_direct.divergence_condition)
        self.assertEqual(result_entry.target_continues_to, result_direct.target_continues_to)
        self.assertEqual(result_entry.proximal_continues_to, result_direct.proximal_continues_to)

    def test_returns_proximal_test_instance(self):
        unit = _unit("simple", start=5, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2, 5])
        p    = _proximal("t", visited=[1, 2, 3])

        result = analyze_divergence(p, tp, SIMPLE_SOURCE)
        self.assertIsInstance(result, PathProximalTest)

    def test_no_divergence_scenario(self):
        """All target nodes covered → fallback messages."""
        unit = _unit("simple", start=5, source_file="")
        tp   = _target_path(unit, path_nodes=[1, 2])
        p    = _proximal("t", visited=[1, 2, 5])

        result = analyze_divergence(p, tp, SIMPLE_SOURCE)
        self.assertIsNone(result.divergence_lineno)
        self.assertEqual(result.divergence_condition, "(could not pinpoint divergence)")


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    unittest.main(verbosity=2)
