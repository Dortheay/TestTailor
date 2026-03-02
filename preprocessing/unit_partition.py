"""
Unit Partition
==============
Partition uncovered code into the smallest contiguous execution units.

A *unit* is either:
  - A linear sequence of statements (no branching constructs inside)
  - A minimal branching construct (if/elif/else, for, while, try/except)
    whose body does NOT contain further nested conditionals at the top level.

This is intentionally coarser than a basic block: we keep semantically
self-contained logic chunks that LLMs can understand in one shot.
"""

import ast
import textwrap
from typing import List, Set, Tuple, Optional
from pathlib import Path

from models import CodeUnit


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _has_nested_conditional(node: ast.AST) -> bool:
    """
    Return True if *node*'s direct children contain another conditional
    (if/for/while/try/with) at the *top* level of its body.
    We only look one level deep because that is the criterion for splitting.
    """
    body = []
    if isinstance(node, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
        body = getattr(node, 'body', []) + getattr(node, 'orelse', []) + \
               getattr(node, 'handlers', []) + getattr(node, 'finalbody', [])
    for child in body:
        if isinstance(child, (ast.If, ast.For, ast.While, ast.Try, ast.With)):
            return True
    return False


def _node_is_branching(node: ast.AST) -> bool:
    return isinstance(node, (ast.If, ast.For, ast.While, ast.Try,
                              ast.With, ast.AsyncFor, ast.AsyncWith))


def _source_lines(source: str, node: ast.AST) -> Tuple[int, int]:
    """Return (start_lineno, end_lineno) for an AST node (1-indexed)."""
    return node.lineno, node.end_lineno


# ──────────────────────────────────────────────────────────────────────────────
# Core partitioner
# ──────────────────────────────────────────────────────────────────────────────

class UnitPartitioner:
    """
    Given a module source and a set of uncovered lines, partitions the
    uncovered code inside every function into CodeUnits.
    """

    def __init__(self, source: str, source_file: str):
        self.source = source
        self.source_file = source_file
        self.source_lines = source.splitlines()
        self.tree = ast.parse(source, filename=source_file)

    # ── Public API ──────────────────────────────────────────────────────────

    def partition(self, uncovered_lines: Set[int]) -> List[CodeUnit]:
        """
        Return a list of CodeUnits covering all *uncovered_lines*.

        Parameters
        ----------
        uncovered_lines:
            Set of 1-indexed line numbers that are not yet covered by any test.
        """
        units: List[CodeUnit] = []
        counter = [0]  # mutable counter for unit IDs

        for func_node in self._iter_functions(self.tree):
            func_uncovered = {
                ln for ln in uncovered_lines
                if func_node.lineno <= ln <= func_node.end_lineno
            }
            if not func_uncovered:
                continue

            func_name = func_node.name
            func_units = self._partition_body(
                func_node.body, func_name, func_uncovered, counter
            )
            units.extend(func_units)

        return units

    # ── Internals ────────────────────────────────────────────────────────────

    def _iter_functions(self, tree: ast.Module):
        """Yield all top-level and nested function/method definitions."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                yield node

    def _partition_body(
        self,
        stmts: List[ast.stmt],
        func_name: str,
        uncovered: Set[int],
        counter: List[int],
    ) -> List[CodeUnit]:
        """
        Recursively partition a list of statements into CodeUnits.
        """
        units: List[CodeUnit] = []
        linear_buffer: List[ast.stmt] = []

        def flush_linear():
            """Flush accumulated linear statements into a unit."""
            if not linear_buffer:
                return
            # Only keep lines that are actually uncovered
            buf_lines = set()
            for s in linear_buffer:
                buf_lines.update(range(s.lineno, s.end_lineno + 1))
            if buf_lines & uncovered:
                start = linear_buffer[0].lineno
                end = linear_buffer[-1].end_lineno
                units.append(self._make_unit(
                    func_name, start, end, "linear", counter
                ))
            linear_buffer.clear()

        for stmt in stmts:
            stmt_lines = set(range(stmt.lineno, stmt.end_lineno + 1))
            stmt_uncovered = stmt_lines & uncovered

            if not stmt_uncovered:
                # This statement is covered – flush any buffered linear stmts
                flush_linear()
                continue

            if not _node_is_branching(stmt):
                # Simple statement: buffer it
                linear_buffer.append(stmt)
            else:
                # Branching statement
                flush_linear()

                if isinstance(stmt, ast.If):
                    # 永远拆分 if/else，而不是整体作为一个 unit
                    units.extend(
                        self._recurse_branching(stmt, func_name, uncovered, counter)
                    )
                elif not _has_nested_conditional(stmt):
                    # Minimal branch: emit as a single unit
                    units.append(self._make_branch_unit(stmt, func_name, counter))
                else:
                    # Has nested conditionals: recurse into sub-bodies
                    units.extend(
                        self._recurse_branching(stmt, func_name, uncovered, counter)
                    )

        flush_linear()
        return units

    def _recurse_branching(
        self,
        node: ast.AST,
        func_name: str,
        uncovered: Set[int],
        counter: List[int],
    ) -> List[CodeUnit]:
        """Recurse into bodies of complex branching nodes."""
        units = []
        sub_bodies = []

        if isinstance(node, ast.If):
            if node.body:
                units.extend(
                    self._partition_body(node.body, func_name, uncovered, counter)
                )
            if node.orelse:
                units.extend(
                    self._partition_body(node.orelse, func_name, uncovered, counter)
                )
            return units
            # sub_bodies.append(("if_body", node.body))
            # if node.orelse:
            #     sub_bodies.append(("else_body", node.orelse))
        elif isinstance(node, (ast.For, ast.While, ast.AsyncFor)):
            sub_bodies.append(("loop_body", node.body))
            if node.orelse:
                sub_bodies.append(("loop_else", node.orelse))
        elif isinstance(node, ast.Try):
            sub_bodies.append(("try_body", node.body))
            for handler in node.handlers:
                sub_bodies.append(("except_body", handler.body))
            if node.orelse:
                sub_bodies.append(("try_else", node.orelse))
            if node.finalbody:
                sub_bodies.append(("finally_body", node.finalbody))
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            sub_bodies.append(("with_body", node.body))

        for _, body in sub_bodies:
            units.extend(
                self._partition_body(body, func_name, uncovered, counter)
            )
        return units

    def _make_unit(
        self,
        func_name: str,
        start: int,
        end: int,
        unit_type: str,
        counter: List[int],
    ) -> CodeUnit:
        counter[0] += 1
        uid = f"{func_name}:unit_{counter[0]}"
        snippet = self._extract_snippet(start, end)
        return CodeUnit(
            unit_id=uid,
            source_file=self.source_file,
            function_name=func_name,
            start_lineno=start,
            end_lineno=end,
            unit_type=unit_type,
            code_snippet=snippet,
        )

    def _make_branch_unit(
        self,
        node: ast.AST,
        func_name: str,
        counter: List[int],
    ) -> CodeUnit:
        counter[0] += 1
        start = node.lineno
        end = node.end_lineno
        uid = f"{func_name}:unit_{counter[0]}"
        snippet = self._extract_snippet(start, end)

        # Extract branch condition string
        condition = None
        if isinstance(node, ast.If):
            condition = ast.unparse(node.test)
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            condition = f"for {ast.unparse(node.target)} in {ast.unparse(node.iter)}"
        elif isinstance(node, ast.While):
            condition = ast.unparse(node.test)

        return CodeUnit(
            unit_id=uid,
            source_file=self.source_file,
            function_name=func_name,
            start_lineno=start,
            end_lineno=end,
            unit_type="branch",
            branch_condition=condition,
            code_snippet=snippet,
        )

    def _extract_snippet(self, start: int, end: int) -> str:
        """Extract source lines and dedent them."""
        lines = self.source_lines[start - 1: end]
        return textwrap.dedent("\n".join(lines))


# ──────────────────────────────────────────────────────────────────────────────
# Convenience function
# ──────────────────────────────────────────────────────────────────────────────

def partition_uncovered(
    source_path: str,
    uncovered_lines: Set[int],
) -> List[CodeUnit]:
    """
    High-level entry point.

    Parameters
    ----------
    source_path : path to the Python module under test
    uncovered_lines : set of 1-indexed uncovered line numbers
    """
    source = Path(source_path).read_text(encoding="utf-8")
    partitioner = UnitPartitioner(source, source_path)
    return partitioner.partition(uncovered_lines)


# ──────────────────────────────────────────────────────────────────────────────
# Manual Test Entry
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from pprint import pprint

    # 被测文件路径
    # test_file = "/Users/dorthea/Documents/research/paperSubmission/FSE2026/TestTailorCode/tests/sample_target.py"

    # # 假设这些行尚未被覆盖（1-indexed）
    # uncovered = {
    #     4, 5,       # simple_function 中部分
    #     9, 10, 11, 12, 13, 14, 15, # if 分支       # else 分支
    #     23, 24,     # for 循环
    # }
    
    test_file = "/Users/dorthea/Documents/research/paperSubmission/FSE2026/TestTailorCode/tests/sample_target_v2.py"

    # 模拟未覆盖行（1-indexed）
    uncovered = {
        # compute
        5,6,7,8,9,10,12,

        # nested_branch
        19,20,21,22,

        # mixed_constructs
        32, 33,
        36, 37,
        40,
    }

    # test_file = "/Users/dorthea/Documents/research/paperSubmission/FSE2026/TestTailorCode/tests/order_management/main.py"
    # uncovered = {
    #     5,7,8,10
    # }
    units = partition_uncovered(test_file, uncovered)

    print("=" * 60)
    print(f"Total Units: {len(units)}")
    print("=" * 60)

    for u in units:
        print(f"Unit ID      : {u.unit_id}")
        print(f"Function     : {u.function_name}")
        print(f"Type         : {u.unit_type}")
        print(f"Lines        : {u.start_lineno}-{u.end_lineno}")
        if getattr(u, "branch_condition", None):
            print(f"Condition    : {u.branch_condition}")
        print("Code Snippet:")
        print(u.code_snippet)
        print("-" * 60)