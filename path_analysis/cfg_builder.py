"""
Control Flow Graph (CFG) Builder
=================================
Builds a CFG from a function's AST body, then computes its dominator tree.
The CFG is used by:
  - PathProximalSelector: to map test execution paths to CFG nodes
  - PathDivergenceAnalyzer: to locate the first divergence point

CFG Node types
--------------
  - ENTRY / EXIT  : pseudo-nodes at function boundaries
  - STATEMENT     : single AST statement (no branching)
  - BRANCH        : if/elif/else decision point
  - LOOP_HEADER   : for/while condition
  - EXCEPTION     : try/except handler
"""

import argparse
import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


# ──────────────────────────────────────────────────────────────────────────────
# Data structures
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class CFGNode:
    node_id: int
    node_type: str          # "entry" | "exit" | "statement" | "branch" | "loop_header"
    lineno: Optional[int]   # source line number (None for ENTRY/EXIT)
    label: str = ""         # human-readable label
    ast_node: Optional[ast.AST] = None
    successors: List[int] = field(default_factory=list)
    predecessors: List[int] = field(default_factory=list)


class CFG:
    """Simple CFG representation."""

    def __init__(self):
        self._nodes: Dict[int, CFGNode] = {}
        self._id_counter = 0
        self.entry_id: Optional[int] = None
        self.exit_id: Optional[int] = None

    def add_node(self, node_type: str, lineno: Optional[int] = None,
                 label: str = "", ast_node=None) -> int:
        nid = self._id_counter
        self._id_counter += 1
        self._nodes[nid] = CFGNode(
            node_id=nid,
            node_type=node_type,
            lineno=lineno,
            label=label,
            ast_node=ast_node,
        )
        return nid

    def add_edge(self, src: int, dst: int):
        if dst not in self._nodes[src].successors:
            self._nodes[src].successors.append(dst)
        if src not in self._nodes[dst].predecessors:
            self._nodes[dst].predecessors.append(src)

    def node(self, nid: int) -> CFGNode:
        return self._nodes[nid]

    @property
    def nodes(self) -> Dict[int, CFGNode]:
        return self._nodes

    def lineno_to_node(self, lineno: int) -> Optional[int]:
        """Find the first CFG node id whose lineno matches."""
        for nid, n in self._nodes.items():
            if n.lineno == lineno:
                return nid
        return None

    def node_for_lineno(self, lineno: int) -> Optional[CFGNode]:
        nid = self.lineno_to_node(lineno)
        return self._nodes[nid] if nid is not None else None


# ──────────────────────────────────────────────────────────────────────────────
# CFG Builder
# ──────────────────────────────────────────────────────────────────────────────

class CFGBuilder:
    """
    Builds a CFG for a single function by walking its AST body.
    Returns a (CFG, function_node_id) pair where function_node_id is ENTRY.
    """

    def __init__(self):
        self.cfg = CFG()

    def build(self, func_node: ast.FunctionDef) -> CFG:
        cfg = self.cfg
        entry = cfg.add_node("entry", label="ENTRY")
        exit_ = cfg.add_node("exit", label="EXIT")
        cfg.entry_id = entry
        cfg.exit_id = exit_

        exits = self._process_body(func_node.body, [entry], exit_)
        for e in exits:
            cfg.add_edge(e, exit_)

        return cfg

    def _process_body(
        self,
        stmts: List[ast.stmt],
        prev_nodes: List[int],
        exit_node: int,
    ) -> List[int]:
        """
        Process a list of statements, threading *prev_nodes* through them.
        Returns the set of 'fall-through' node ids after the last statement.
        """
        current = prev_nodes
        for stmt in stmts:
            current = self._process_stmt(stmt, current, exit_node)
        return current

    def _process_stmt(
        self,
        stmt: ast.stmt,
        prev_nodes: List[int],
        exit_node: int,
    ) -> List[int]:
        cfg = self.cfg

        if isinstance(stmt, (ast.Return, ast.Raise, ast.Break, ast.Continue)):
            nid = cfg.add_node("statement", stmt.lineno,
                               label=ast.unparse(stmt)[:60], ast_node=stmt)
            for p in prev_nodes:
                cfg.add_edge(p, nid)
            # These terminate the current path
            if isinstance(stmt, ast.Return):
                cfg.add_edge(nid, exit_node)
            return []  # no fall-through

        elif isinstance(stmt, ast.If):
            return self._process_if(stmt, prev_nodes, exit_node)

        elif isinstance(stmt, (ast.For, ast.AsyncFor)):
            return self._process_loop(stmt, prev_nodes, exit_node)

        elif isinstance(stmt, ast.While):
            return self._process_while(stmt, prev_nodes, exit_node)

        elif isinstance(stmt, ast.Try):
            return self._process_try(stmt, prev_nodes, exit_node)

        else:
            # Simple statement
            nid = cfg.add_node("statement", stmt.lineno,
                               label=ast.unparse(stmt)[:60], ast_node=stmt)
            for p in prev_nodes:
                cfg.add_edge(p, nid)
            return [nid]

    def _process_if(self, stmt: ast.If, prev: List[int], exit_: int) -> List[int]:
        cfg = self.cfg
        branch = cfg.add_node("branch", stmt.lineno,
                               label=f"if {ast.unparse(stmt.test)[:40]}", ast_node=stmt)
        for p in prev:
            cfg.add_edge(p, branch)

        # True branch
        true_exits = self._process_body(stmt.body, [branch], exit_)

        # False branch (else or fall-through)
        if stmt.orelse:
            false_exits = self._process_body(stmt.orelse, [branch], exit_)
        else:
            false_exits = [branch]  # no else: fall through from branch

        return true_exits + false_exits

    def _process_loop(
        self,
        stmt: ast.For | ast.AsyncFor,
        prev: List[int],
        exit_: int,
    ) -> List[int]:
        cfg = self.cfg
        header = cfg.add_node(
            "loop_header", stmt.lineno,
            label=f"for {ast.unparse(stmt.target)} in {ast.unparse(stmt.iter)[:30]}",
            ast_node=stmt,
        )
        for p in prev:
            cfg.add_edge(p, header)

        body_exits = self._process_body(stmt.body, [header], exit_)
        # Loop back edge
        for e in body_exits:
            cfg.add_edge(e, header)

        # After-loop exits (loop condition false, or else branch)
        if stmt.orelse:
            return self._process_body(stmt.orelse, [header], exit_)
        return [header]  # exits when loop ends

    def _process_while(self, stmt: ast.While, prev: List[int], exit_: int) -> List[int]:
        cfg = self.cfg
        header = cfg.add_node(
            "loop_header", stmt.lineno,
            label=f"while {ast.unparse(stmt.test)[:40]}",
            ast_node=stmt,
        )
        for p in prev:
            cfg.add_edge(p, header)

        body_exits = self._process_body(stmt.body, [header], exit_)
        for e in body_exits:
            cfg.add_edge(e, header)

        if stmt.orelse:
            return self._process_body(stmt.orelse, [header], exit_)
        return [header]

    def _process_try(self, stmt: ast.Try, prev: List[int], exit_: int) -> List[int]:
        cfg = self.cfg
        try_entry = cfg.add_node("statement", stmt.lineno, label="try:", ast_node=stmt)
        for p in prev:
            cfg.add_edge(p, try_entry)

        body_exits = self._process_body(stmt.body, [try_entry], exit_)
        handler_exits = []
        for handler in stmt.handlers:
            h = cfg.add_node("exception", handler.lineno,
                              label=f"except {handler.type and ast.unparse(handler.type) or ''}",
                              ast_node=handler)
            cfg.add_edge(try_entry, h)
            handler_exits.extend(self._process_body(handler.body, [h], exit_))

        all_exits = body_exits + handler_exits
        if stmt.orelse:
            all_exits = self._process_body(stmt.orelse, all_exits, exit_)
        if stmt.finalbody:
            all_exits = self._process_body(stmt.finalbody, all_exits, exit_)
        return all_exits


# ──────────────────────────────────────────────────────────────────────────────
# Dominator Tree
# ──────────────────────────────────────────────────────────────────────────────

class DominatorTree:
    """
    Simple dominator tree computed from a CFG using the iterative algorithm.
    dom[n] = immediate dominator of n.
    """

    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self.idom: Dict[int, Optional[int]] = {}  # node_id → immediate dominator
        self.children: Dict[int, List[int]] = {}  # node_id → dominated nodes
        self._compute()

    def _compute(self):
        cfg = self.cfg
        entry = cfg.entry_id
        all_nodes = list(cfg.nodes.keys())

        # Reverse post-order
        rpo = self._reverse_postorder(entry, all_nodes)
        rpo_index = {n: i for i, n in enumerate(rpo)}

        idom: Dict[int, Optional[int]] = {entry: entry}
        changed = True
        while changed:
            changed = False
            for b in rpo:
                if b == entry:
                    continue
                preds = [p for p in cfg.node(b).predecessors if p in idom]
                if not preds:
                    continue
                new_idom = preds[0]
                for p in preds[1:]:
                    if p in idom:
                        new_idom = self._intersect(p, new_idom, idom, rpo_index)
                if idom.get(b) != new_idom:
                    idom[b] = new_idom
                    changed = True

        self.idom = idom
        self.children = {n: [] for n in all_nodes}
        for n, d in idom.items():
            if n != entry and d is not None:
                self.children.setdefault(d, []).append(n)

    def _intersect(
        self,
        b1: int, b2: int,
        idom: Dict[int, Optional[int]],
        rpo_index: Dict[int, int],
    ) -> int:
        finger1, finger2 = b1, b2
        while finger1 != finger2:
            while rpo_index.get(finger1, 0) > rpo_index.get(finger2, 0):
                finger1 = idom[finger1]
            while rpo_index.get(finger2, 0) > rpo_index.get(finger1, 0):
                finger2 = idom[finger2]
        return finger1

    def _reverse_postorder(self, entry: int, all_nodes: List[int]) -> List[int]:
        visited: Set[int] = set()
        postorder: List[int] = []

        def dfs(n: int):
            visited.add(n)
            for s in self.cfg.node(n).successors:
                if s not in visited:
                    dfs(s)
            postorder.append(n)

        dfs(entry)
        return list(reversed(postorder))

    def get_siblings(self, node_id: int) -> List[int]:
        """Return sibling nodes (same immediate dominator, excluding node_id)."""
        dom = self.idom.get(node_id)
        if dom is None or dom == node_id:
            return []
        return [c for c in self.children.get(dom, []) if c != node_id]

    def get_parent(self, node_id: int) -> Optional[int]:
        dom = self.idom.get(node_id)
        return dom if dom != node_id else None

    def ancestors(self, node_id: int) -> List[int]:
        """Return ancestor node ids from root to node_id (exclusive)."""
        result = []
        current = self.idom.get(node_id)
        visited = set()
        while current is not None and current != node_id and current not in visited:
            visited.add(current)
            result.append(current)
            next_ = self.idom.get(current)
            if next_ == current:
                break
            current = next_
        return list(reversed(result))


# ──────────────────────────────────────────────────────────────────────────────
# Convenience
# ──────────────────────────────────────────────────────────────────────────────

def build_cfg(func_node: ast.FunctionDef) -> Tuple[CFG, DominatorTree]:
    """Build CFG + dominator tree for a function. Returns (cfg, dom_tree)."""
    builder = CFGBuilder()
    cfg = builder.build(func_node)
    dom = DominatorTree(cfg)
    return cfg, dom


# ──────────────────────────────────────────────────────────────────────────────
# CLI helpers
# ──────────────────────────────────────────────────────────────────────────────

def build_cfg_from_file(source_path: str, function_name: str) -> Tuple[CFG, DominatorTree]:
    """
    Convenience helper: parse *source_path*, locate *function_name* and
    return (cfg, dom_tree) for that function.
    """
    path = Path(source_path)
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    target_func: Optional[ast.FunctionDef] = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            target_func = node
            break

    if target_func is None:
        raise ValueError(f"Function {function_name!r} not found in {source_path}")

    return build_cfg(target_func)


def _format_cfg_for_cli(cfg: CFG, dom: DominatorTree) -> str:
    """
    Produce a human-readable text representation of the CFG and dominators,
    suitable for printing from a small CLI.
    """
    lines: List[str] = []
    lines.append("CFG Nodes")
    lines.append("=========")
    for nid in sorted(cfg.nodes.keys()):
        node = cfg.node(nid)
        idom = dom.idom.get(nid)
        lineno_display = node.lineno if node.lineno is not None else "-"
        lines.append(
            f"[{nid:02d}] type={node.node_type:<11} "
            f"lineno={lineno_display!s:>4} "
            f"label={node.label!r} "
            f"idom={idom if idom is not None else '-'}"
        )
        lines.append(
            f"      succ={sorted(node.successors)}  "
            f"pred={sorted(node.predecessors)}"
        )
    return "\n".join(lines)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build and inspect a control-flow graph (CFG) for a single function "
            "in a Python source file."
        )
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the Python source file containing the target function.",
    )
    parser.add_argument(
        "--func",
        required=True,
        help="Name of the function to analyze.",
    )
    return parser.parse_args()


def main() -> None:
    """
    Small CLI entry point so you can quickly inspect the CFG of a function.

    Example:
        python -m path_analysis.cfg_builder --file tests/sample_target.py --func simple_function
    """
    args = _parse_args()
    cfg, dom = build_cfg_from_file(args.file, args.func)
    print(_format_cfg_for_cli(cfg, dom))


if __name__ == "__main__":
    main()
