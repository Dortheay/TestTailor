"""
Symbolic Constraint Extractor
==============================
Extracts path constraints from the target path to a CodeUnit using a
lightweight symbolic / static approach:

  1. Traverse the AST upward from the target unit to the function root
     to build the *target path template*.
  2. For each branch/loop on the path, collect the guarding predicate
     with two special-case treatments:
       - Loop-aware hints  : record the loop guard AND an iteration-count hint
       - Elif-chain pruning: negate all earlier arms so only the intended
                             arm's condition is selected.

Returns a TargetPath (with a list of PathConstraints) ready to be embedded
into the LLM prompt.
"""

import argparse
import ast
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# Ensure project root (where models.py lives) is importable when running this
# file directly as a script.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models import CodeUnit, PathConstraint, TargetPath


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _unparse(node: ast.AST) -> str:
    return ast.unparse(node)


def _negate(expr: str) -> str:
    """Wrap an expression in 'not (...)' for elif-chain pruning."""
    return f"not ({expr})"


def _is_elif_chain(parent: ast.If, child: ast.If) -> bool:
    """Return True if *child* is an elif arm of *parent* (i.e., in orelse)."""
    return (len(parent.orelse) == 1 and
            isinstance(parent.orelse[0], ast.If) and
            parent.orelse[0] is child)


# ──────────────────────────────────────────────────────────────────────────────
# Parent map
# ──────────────────────────────────────────────────────────────────────────────

def _build_parent_map(tree: ast.AST) -> dict:
    """Map each AST node to its parent."""
    parents = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parents[id(child)] = node
    return parents


# ──────────────────────────────────────────────────────────────────────────────
# Path builder
# ──────────────────────────────────────────────────────────────────────────────

def _build_path_from_unit_to_root(
    unit: CodeUnit,
    func_node: ast.FunctionDef,
    source: str,
) -> List[ast.AST]:
    """
    Walk the AST from *func_node* and return the list of ancestor nodes
    (inclusive from *func_node* to the first statement of the target unit).
    Order: [func_node, outer_branch, ..., direct_parent_of_unit].
    """
    parent_map = _build_parent_map(func_node)

    # Find the AST node(s) at the target unit's start line
    target_node = _find_node_at_line(func_node, unit.start_lineno)
    if target_node is None:
        return []

    # Walk up via parent_map
    path: List[ast.AST] = []
    current = target_node
    while current is not None and current is not func_node:
        path.append(current)
        current = parent_map.get(id(current))
    path.append(func_node)
    path.reverse()  # now from func_node down to target
    return path


def _find_node_at_line(root: ast.AST, lineno: int) -> Optional[ast.AST]:
    """Find the first AST node whose lineno matches."""
    for node in ast.walk(root):
        if getattr(node, 'lineno', None) == lineno:
            return node
    return None


# ──────────────────────────────────────────────────────────────────────────────
# Constraint extractor
# ──────────────────────────────────────────────────────────────────────────────

class SymbolicConstraintExtractor:
    """
    Extracts PathConstraints for the target path from function entry to unit.
    """

    def __init__(self, source: str):
        self.source = source
        self.tree = ast.parse(source)

    def extract(self, unit: CodeUnit) -> TargetPath:
        """
        Build the TargetPath with all constraints for *unit*.
        """
        func_node = self._find_function(unit.function_name)
        if func_node is None:
            return TargetPath(unit=unit)

        ancestor_path = _build_path_from_unit_to_root(unit, func_node, self.source)
        constraints = self._collect_constraints(ancestor_path, unit)
        path_nodes = [getattr(n, 'lineno', 0) for n in ancestor_path
                      if getattr(n, 'lineno', None)]

        return TargetPath(unit=unit, constraints=constraints, path_nodes=path_nodes)

    # ── Core constraint collection ──────────────────────────────────────────

    def _collect_constraints(
        self,
        path: List[ast.AST],
        unit: CodeUnit,
    ) -> List[PathConstraint]:
        """
        Iterate over the ancestor path and emit a PathConstraint for each
        decision point that the target path must satisfy.
        """
        constraints: List[PathConstraint] = []
        elif_negations: List[str] = []  # accumulated negations for elif-chain

        for i, node in enumerate(path):
            # ── If/elif/else ──────────────────────────────────────────────
            if isinstance(node, ast.If):
                child = path[i + 1] if i + 1 < len(path) else None
                cond_str = _unparse(node.test)

                # Elif-chain pruning: check if this is part of an elif chain
                is_elif = (i > 0 and isinstance(path[i - 1], ast.If) and
                           _is_elif_chain(path[i - 1], node))

                # Determine which branch (true / false) the target path takes
                true_branch_nodes = [id(n) for n in ast.walk(node)
                                     if n in getattr(node, 'body', [])]

                if child is not None and id(child) in [id(n) for n in node.body]:
                    # Target goes into the True branch
                    # For elif chains, prepend negations of all earlier arms
                    full_cond = self._apply_elif_negations(cond_str, elif_negations)
                    constraints.append(PathConstraint(
                        condition=full_cond,
                        negated=False,
                        constraint_type="elif" if elif_negations else "branch",
                        lineno=node.lineno,
                    ))
                    elif_negations = []  # reset on entering a branch

                elif child is not None and id(child) in self._collect_ids(node.orelse):
                    # Target goes into the False branch (else / next elif)
                    # Negate this arm and accumulate for elif chain
                    elif_negations.append(cond_str)
                    full_cond = self._apply_elif_negations(
                        _negate(cond_str), elif_negations[:-1]
                    )
                    constraints.append(PathConstraint(
                        condition=full_cond,
                        negated=True,
                        constraint_type="branch",
                        lineno=node.lineno,
                    ))

            # ── For loops ────────────────────────────────────────────────
            elif isinstance(node, (ast.For, ast.AsyncFor)):
                child = path[i + 1] if i + 1 < len(path) else None
                if child is not None and id(child) in self._collect_ids(node.body):
                    iter_str = _unparse(node.iter)
                    target_str = _unparse(node.target)
                    loop_hint = self._estimate_loop_iterations(node, unit)
                    constraints.append(PathConstraint(
                        condition=f"for {target_str} in {iter_str}",
                        negated=False,
                        constraint_type="loop_entry",
                        loop_count_hint=loop_hint,
                        lineno=node.lineno,
                    ))

            # ── While loops ──────────────────────────────────────────────
            elif isinstance(node, ast.While):
                child = path[i + 1] if i + 1 < len(path) else None
                if child is not None and id(child) in self._collect_ids(node.body):
                    cond_str = _unparse(node.test)
                    loop_hint = self._estimate_loop_iterations(node, unit)
                    constraints.append(PathConstraint(
                        condition=cond_str,
                        negated=False,
                        constraint_type="loop_entry",
                        loop_count_hint=loop_hint,
                        lineno=node.lineno,
                    ))

            # ── Try/except ──────────────────────────────────────────────
            elif isinstance(node, ast.Try):
                child = path[i + 1] if i + 1 < len(path) else None
                if child is not None:
                    in_handler = id(child) in self._collect_ids(
                        [h.body[0] for h in node.handlers if h.body]
                    )
                    if in_handler:
                        # Target is in an exception handler
                        for handler in node.handlers:
                            if id(child) in self._collect_ids(handler.body):
                                exc_type = (
                                    _unparse(handler.type) if handler.type else "Exception"
                                )
                                constraints.append(PathConstraint(
                                    condition=f"raises {exc_type}",
                                    negated=False,
                                    constraint_type="branch",
                                    lineno=node.lineno,
                                ))

        return constraints

    # ── Utilities ───────────────────────────────────────────────────────────

    def _apply_elif_negations(self, cond: str, negations: List[str]) -> str:
        if not negations:
            return cond
        neg_parts = " and ".join(f"not ({n})" for n in negations)
        return f"{neg_parts} and {cond}"

    def _collect_ids(self, nodes) -> set:
        """Collect id() of all nodes in the given list/body recursively."""
        result = set()
        for n in (nodes or []):
            result.add(id(n))
            for child in ast.walk(n):
                result.add(id(child))
        return result

    def _find_function(
        self, func_name: str
    ) -> Optional[ast.FunctionDef]:
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name == func_name:
                    return node
        return None

    def _estimate_loop_iterations(
        self,
        node: ast.AST,
        unit: CodeUnit,
    ) -> int:
        """
        Heuristic: estimate how many loop iterations are needed to reach the
        target unit.  Falls back to 1 (first iteration) if we cannot determine.
        """
        # If the target is inside the loop body at a statement after the
        # loop header, we need at least 1 iteration.
        # TODO: a more precise analysis would inspect rfind-like patterns
        #       (as in the paper's motivating example with rfind("\n"...) + 1).
        return 1


# ──────────────────────────────────────────────────────────────────────────────
# Constraint → human-readable string
# ──────────────────────────────────────────────────────────────────────────────

def format_constraints(target_path: TargetPath) -> str:
    """
    Render the constraints as a readable block for LLM prompt insertion.
    """
    if not target_path.constraints:
        return "(no additional path constraints)"

    lines = []
    for pc in target_path.constraints:
        prefix = ""
        if pc.constraint_type == "loop_entry":
            hint = (f" (must execute at least {pc.loop_count_hint} time(s))"
                    if pc.loop_count_hint else "")
            lines.append(f"  - Loop entry: {pc.condition}{hint}")
        elif pc.constraint_type in ("elif", "branch"):
            lines.append(f"  - Condition must be True: {pc.condition}")
        else:
            lines.append(f"  - {pc.condition}")

    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Convenience entry point
# ──────────────────────────────────────────────────────────────────────────────

def extract_constraints(unit: CodeUnit, source: str) -> TargetPath:
    """High-level entry point."""
    extractor = SymbolicConstraintExtractor(source)
    return extractor.extract(unit)


# ──────────────────────────────────────────────────────────────────────────────
# CLI helpers
# ──────────────────────────────────────────────────────────────────────────────

def build_target_path_from_file(
    source_path: str,
    function_name: str,
    start_lineno: int,
    end_lineno: Optional[int] = None,
    unit_type: str = "linear",
    unit_id: Optional[str] = None,
) -> TargetPath:
    """
    Convenience helper for manual experimentation.

    It constructs a minimal CodeUnit for the given function and line range,
    then runs symbolic constraint extraction on it and returns the TargetPath.
    """
    path = Path(source_path)
    source = path.read_text(encoding="utf-8")

    if end_lineno is None:
        end_lineno = start_lineno

    if unit_id is None:
        unit_id = f"{function_name}:{start_lineno}-{end_lineno}"

    unit = CodeUnit(
        unit_id=unit_id,
        source_file=str(path),
        function_name=function_name,
        start_lineno=start_lineno,
        end_lineno=end_lineno,
        unit_type=unit_type,
        code_snippet="",
    )
    return extract_constraints(unit, source)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract symbolic path constraints for reaching a given code unit "
            "inside a function."
        )
    )
    parser.add_argument(
        "--file",
        required=True,
        help="包含目标函数的 Python 源文件路径",
    )
    parser.add_argument(
        "--func",
        required=True,
        help="目标函数名称",
    )
    parser.add_argument(
        "--start-line",
        type=int,
        required=True,
        help="目标 CodeUnit 的起始行号（包含）",
    )
    parser.add_argument(
        "--end-line",
        type=int,
        default=None,
        help="目标 CodeUnit 的结束行号（包含），默认为 start-line",
    )
    parser.add_argument(
        "--unit-type",
        default="linear",
        choices=["linear", "branch", "loop"],
        help="CodeUnit 类型，仅用于标注，默认 linear",
    )
    parser.add_argument(
        "--unit-id",
        default=None,
        help="可选：自定义 CodeUnit ID（默认 func:start-end）",
    )
    return parser.parse_args()


def main() -> None:
    """
    小型 CLI 入口，方便快速测试约束提取逻辑。

    示例：
        python -m path_analysis.symbolic_executor \\
            --file tests/sample_target_v2.py \\
            --func mixed_constructs \\
            --start-line 31 --end-line 41
    """
    args = _parse_args()
    target_path = build_target_path_from_file(
        source_path=args.file,
        function_name=args.func,
        start_lineno=args.start_line,
        end_lineno=args.end_line,
        unit_type=args.unit_type,
        unit_id=args.unit_id,
    )

    print("TargetPath")
    print("==========")
    print(f"Unit      : {target_path.unit}")
    print(f"Path nodes: {target_path.path_nodes}")
    print()
    print("Path constraints:")
    print(format_constraints(target_path))


if __name__ == "__main__":
    main()
