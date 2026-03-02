"""
Path-Proximal Test Selector
============================
Implements Algorithm 1 from the paper:

    FindSeedTest(B_target, S_tests, G_CFG, T_Dom)

The algorithm uses a hierarchical search over the dominator tree:
  1. Sibling-level search : tests covering any sibling of the target node
  2. Ancestor-level fallback : ascend to the parent and repeat

Candidates at each level are ranked by Jaccard similarity between their
runtime paths and the target path template.  Ties are broken by choosing
the test whose suffix beyond the common prefix is shortest.
"""

import ast
from typing import Dict, List, Optional, Set, Tuple

from models import CodeUnit, ExecutionPath, PathProximalTest, TargetPath
from path_analysis.cfg_builder import CFG, DominatorTree, build_cfg


# ──────────────────────────────────────────────────────────────────────────────
# Jaccard helpers
# ──────────────────────────────────────────────────────────────────────────────

def _jaccard(a: Set[int], b: Set[int]) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)


def _common_prefix_length(a: List[int], b: List[int]) -> int:
    length = 0
    for x, y in zip(a, b):
        if x == y:
            length += 1
        else:
            break
    return length


def _suffix_length_after_prefix(path: List[int], prefix_len: int) -> int:
    return max(0, len(path) - prefix_len)


# ──────────────────────────────────────────────────────────────────────────────
# Selector
# ──────────────────────────────────────────────────────────────────────────────

class PathProximalSelector:
    """
    Given a target CodeUnit and a collection of test execution paths,
    find the most path-proximal test using Algorithm 1.

    Parameters
    ----------
    cfg : CFG of the function containing the target unit
    dom : Dominator tree of that CFG
    target_path : TargetPath (structural path template)
    """

    def __init__(self, cfg: CFG, dom: DominatorTree, target_path: TargetPath):
        self.cfg = cfg
        self.dom = dom
        self.target_path = target_path
        self._target_node_id = self._find_target_node()
        self._target_line_set = set(target_path.path_nodes)

    def select(
        self,
        execution_paths: Dict[str, ExecutionPath],
    ) -> Optional[PathProximalTest]:
        """
        Run Algorithm 1 and return the most path-proximal test, or None.

        Parameters
        ----------
        execution_paths : dict of test_id → ExecutionPath
        """
        target_nid = self._target_node_id
        if target_nid is None:
            # Fallback: just pick the test with most line overlap
            return self._global_fallback(execution_paths)

        # ── Level 0: sibling search ──────────────────────────────────────
        scope_nids = self.dom.get_siblings(target_nid)
        current_scope = scope_nids

        while current_scope:
            # Lines covered by nodes in the current scope
            scope_lines = self._nodes_to_lines(current_scope)
            candidates = self._find_covering_tests(scope_lines, execution_paths)

            if candidates:
                return self._rank_candidates(candidates, execution_paths)

            # Ascend: get parent and its siblings
            parent = self.dom.get_parent(
                current_scope[0] if current_scope else target_nid
            )
            if parent is None:
                break
            current_scope = self.dom.get_siblings(parent) + [parent]

        # ── Last resort: global fallback ────────────────────────────────
        return self._global_fallback(execution_paths)

    # ── Internals ────────────────────────────────────────────────────────────

    def _find_target_node(self) -> Optional[int]:
        unit = self.target_path.unit
        return self.cfg.lineno_to_node(unit.start_lineno)

    def _nodes_to_lines(self, node_ids: List[int]) -> Set[int]:
        lines: Set[int] = set()
        for nid in node_ids:
            node = self.cfg.nodes.get(nid)
            if node and node.lineno is not None:
                lines.add(node.lineno)
        return lines

    def _find_covering_tests(
        self,
        scope_lines: Set[int],
        execution_paths: Dict[str, ExecutionPath],
    ) -> List[str]:
        """Return test IDs that cover at least one line in scope_lines."""
        return [
            tid for tid, ep in execution_paths.items()
            if ep.covered_lines & scope_lines
        ]

    def _rank_candidates(
        self,
        candidate_ids: List[str],
        execution_paths: Dict[str, ExecutionPath],
    ) -> Optional[PathProximalTest]:
        """
        Rank by (Jaccard DESC, suffix_length ASC) and return the best.
        """
        target_lines = self._target_line_set
        target_seq = self.target_path.path_nodes

        best_tid: Optional[str] = None
        best_sim: float = -1.0
        best_suffix: int = 10 ** 9

        for tid in candidate_ids:
            ep = execution_paths[tid]
            sim = _jaccard(ep.covered_lines, target_lines)
            prefix_len = _common_prefix_length(ep.visited_nodes, target_seq)
            suffix = _suffix_length_after_prefix(ep.visited_nodes, prefix_len)

            if (sim > best_sim) or (sim == best_sim and suffix < best_suffix):
                best_sim = sim
                best_suffix = suffix
                best_tid = tid

        if best_tid is None:
            return None

        ep = execution_paths[best_tid]
        return PathProximalTest(
            test_id=best_tid,
            test_source=ep.test_source,
            execution_path=ep,
            jaccard_similarity=best_sim,
        )

    def _global_fallback(
        self,
        execution_paths: Dict[str, ExecutionPath],
    ) -> Optional[PathProximalTest]:
        """Fall back to the test with the most line-level overlap."""
        if not execution_paths:
            return None
        target_lines = self._target_line_set
        best = max(
            execution_paths.items(),
            key=lambda kv: _jaccard(kv[1].covered_lines, target_lines),
        )
        tid, ep = best
        return PathProximalTest(
            test_id=tid,
            test_source=ep.test_source,
            execution_path=ep,
            jaccard_similarity=_jaccard(ep.covered_lines, target_lines),
        )


# ──────────────────────────────────────────────────────────────────────────────
# Convenience entry point
# ──────────────────────────────────────────────────────────────────────────────

def find_path_proximal_test(
    unit: CodeUnit,
    target_path: TargetPath,
    execution_paths: Dict[str, ExecutionPath],
    func_node: ast.FunctionDef,
) -> Optional[PathProximalTest]:
    """
    High-level entry point.

    Parameters
    ----------
    unit          : the uncovered target unit
    target_path   : structural path template with constraints
    execution_paths : dict of test_id → ExecutionPath (from TraceCollector)
    func_node     : AST node of the enclosing function
    """
    cfg, dom = build_cfg(func_node)
    selector = PathProximalSelector(cfg, dom, target_path)
    return selector.select(execution_paths)
