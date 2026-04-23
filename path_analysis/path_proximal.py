import os
import argparse
import json
from typing import List, Set, Dict, Optional, Tuple
from pathlib import Path

# Import functionality from existing modules
from models import CodeUnit, ExecutionPath
from path_analysis.cfg_builder import build_cfg_from_file, CFG, DominatorTree
from execution.trace_collector import collect_test_suite_traces

class PathProximalSelector:
    """
    Path-Nearest Selector: 
    Uses a dominator-tree hierarchical search algorithm to locate the existing test that is closest to the target uncovered unit.
    """

    def __init__(self, target_file: str, function_name: str):
        self.target_file = os.path.realpath(target_file)
        self.function_name = function_name
        # 1. Build CFG and dominator tree
        self.cfg, self.dom_tree = build_cfg_from_file(target_file, function_name)

    def get_structural_skeleton(self, target_lineno: int) -> Set[int]:
        """
        Derive the structural path skeleton from the function entry to the target line 
        (i.e., the set of line numbers corresponding to all mandatory nodes along the path).
        """
        node = self.cfg.node_for_lineno(target_lineno)
        if not node:
            return set()

        # Retrieve ancestor nodes in the dominator tree (all mandatory nodes that must be passed to reach this node)
        ancestor_ids = self.dom_tree.ancestors(node.node_id)
        
        # Extract line numbers
        skeleton_lines = {self.cfg.node(nid).lineno for nid in ancestor_ids 
                          if self.cfg.node(nid).lineno is not None}
        if node.lineno:
            skeleton_lines.add(node.lineno)
            
        return skeleton_lines

    def calculate_jaccard(self, set_a: Set[int], set_b: Set[int]) -> float:
        """Calculate Jaccard similarity"""
        if not set_a or not set_b:
            return 0.0
        intersection = len(set_a.intersection(set_b))
        union = len(set_a.union(set_b))
        return intersection / union

    def select_best_test(
        self, 
        target_unit: CodeUnit, 
        test_paths: Dict[str, ExecutionPath]
    ) -> Optional[Tuple[str, float]]:
        """
        
        """
        print(f"\n[Start Search] Target Unit: {target_unit.unit_id} (Line: {target_unit.start_lineno})")
        
        target_node = self.cfg.node_for_lineno(target_unit.start_lineno)
        if not target_node:
            print(f"[!] Error: Cannot find node for line {target_unit.start_lineno} in CFG. Executing global fallback.")
            return self._global_fallback(target_unit, test_paths)

        target_skeleton = self.get_structural_skeleton(target_unit.start_lineno)
        print(f"[*] Target Path Skeleton (Mandatory Lines): {sorted(list(target_skeleton))}")

        current_node_id = target_node.node_id
        level = 0

        # Hierarchical search
        while current_node_id is not None:
            curr_node = self.cfg.node(current_node_id)
            print(f"\n--- [Level {level}] Searching Node ID: {current_node_id} ({curr_node.node_type}) ---")

            # 1. Find sibling nodes
            siblings = self.dom_tree.get_siblings(current_node_id)
            sibling_lines = {self.cfg.node(sid).lineno for sid in siblings 
                             if self.cfg.node(sid).lineno is not None}
            
            print(f"  > Dominator tree sibling node IDs: {siblings}")
            print(f"  > Line numbers associated with sibling nodes: {list(sibling_lines)}")

            if not sibling_lines:
                print(f"  > No valid sibling line numbers at this level. Skipping test matching.")
            else:
                # 2. Search candidate tests at the current level
                candidates = {}
                print(f"  > Scanning {len(test_paths)} test traces...")
                
                for test_id, path in test_paths.items():
                    # Check whether the test covers any sibling node
                    intersection = path.covered_lines.intersection(sibling_lines)
                    if intersection:
                        score = self.calculate_jaccard(target_skeleton, path.covered_lines)
                        candidates[test_id] = score
                        print(f"    [MATCH] Test '{test_id}' hits sibling lines {list(intersection)}, Jaccard: {score:.4f}")
                    else:
                        # Optional: print skipped information (can be commented out if too many tests)
                        # print(f"    [SKIP] Test '{test_id}' does not hit sibling lines")
                        pass

                if candidates:
                    # Algorithm 1 tie-break: among candidates with equal Jaccard,
                    # pick the one whose execution path has the SHORTEST suffix
                    # after the target skeleton (i.e., least extra divergent work).
                    def _suffix_len(tid: str) -> int:
                        ep = test_paths[tid]
                        visited = list(ep.visited_nodes) if ep.visited_nodes else sorted(ep.covered_lines)
                        # suffix = lines executed after the last line that is in target_skeleton
                        last_idx = -1
                        for i, ln in enumerate(visited):
                            if ln in target_skeleton:
                                last_idx = i
                        if last_idx < 0:
                            return len(visited)
                        return len(visited) - last_idx - 1

                    best_id, best_score = max(
                        candidates.items(),
                        key=lambda x: (x[1], -_suffix_len(x[0])),
                    )
                    print(
                        f"\n[+] Best match found at Level {level}: {best_id} "
                        f"(Jaccard: {best_score:.4f}, suffix_len: {_suffix_len(best_id)})"
                    )
                    return best_id, best_score
                else:
                    print(f"  > No tests covering sibling nodes found at Level {level}.")

            # 3. Move upward in the dominator tree
            parent_id = self.dom_tree.get_parent(current_node_id)
            if parent_id is not None and parent_id != current_node_id:
                print(f"  > Backtracking upward: from node {current_node_id} to parent node {parent_id}")
                current_node_id = parent_id
                level += 1
            else:
                print(f"  > Reached the root of the dominator tree.")
                break

        print(f"\n[*] Hierarchical search failed. Entering global similarity computation (Fallback)...")
        return self._global_fallback(target_unit, test_paths)

    def _global_fallback(self, target_unit, test_paths):
        target_skeleton = self.get_structural_skeleton(target_unit.start_lineno)
        print(f"[*] Performing global Jaccard similarity comparison...")

        results = []
        for tid, p in test_paths.items():
            score = self.calculate_jaccard(target_skeleton, p.covered_lines)
            visited = list(p.visited_nodes) if p.visited_nodes else sorted(p.covered_lines)
            last_idx = -1
            for i, ln in enumerate(visited):
                if ln in target_skeleton:
                    last_idx = i
            suffix_len = (len(visited) - last_idx - 1) if last_idx >= 0 else len(visited)
            results.append((tid, score, suffix_len))

        if not results:
            return None

        # Primary: max Jaccard; tie-break: min suffix length (Algorithm 1)
        best = max(results, key=lambda x: (x[1], -x[2]))
        print(f"[+] Globally closest test: {best[0]} (Score: {best[1]:.4f}, suffix: {best[2]})")
        return best[0], best[1]

def load_tests_from_dir(tests_dir: str) -> Dict[str, str]:
    """Load source code of all test files from a directory."""
    test_suite = {}
    dir_path = Path(tests_dir)
    if not dir_path.exists():
        return {}
    for path in dir_path.glob("test_*.py"):
        test_suite[path.stem] = path.read_text(encoding="utf-8")
    return test_suite

def find_path_proximal_test(unit, target_path, execution_paths, func_node=None):
    """
    Public entry used by main.py (Algorithm 1).

    Returns a PathProximalTest or None.
    """
    from models import PathProximalTest
    try:
        selector = PathProximalSelector(unit.source_file, unit.function_name)
    except Exception as e:
        print(f"[find_path_proximal_test] selector init failed: {e}")
        return None
    result = selector.select_best_test(unit, execution_paths)
    if not result:
        return None
    test_id, score = result
    ep = execution_paths.get(test_id)
    if ep is None:
        return None
    return PathProximalTest(
        test_id=test_id,
        test_source=ep.test_source,
        execution_path=ep,
        jaccard_similarity=score,
    )

# ──────────────────────────────────────────────────────────────────────────────
# Main Function
# ──────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Path Proximal Selector CLI")
    parser.add_argument("--target-file", required=True, help="Target source file path")
    parser.add_argument("--func", required=True, help="Target function name")
    parser.add_argument("--line", type=int, required=True, help="Line number of the uncovered target")
    parser.add_argument("--tests-dir", required=True, help="Directory containing existing test cases")
    
    args = parser.parse_args()

    # 1. Construct CodeUnit
    unit = CodeUnit(
        unit_id=f"{args.func}:{args.line}",
        source_file=args.target_file,
        function_name=args.func,
        start_lineno=args.line,
        end_lineno=args.line,
        unit_type="linear",
        code_snippet=""
    )

    # 2. Collect execution traces from existing tests
    print(f"[*] Loading tests from {args.tests_dir} and collecting execution traces...")
    test_sources = load_tests_from_dir(args.tests_dir)
    if not test_sources:
        print(f"[-] No test_*.py files found in {args.tests_dir}")
        return

    traces = collect_test_suite_traces(test_sources, args.target_file)

    # 3. Perform path proximity analysis
    print(f"[*] Analyzing control flow structure of function {args.func}...")
    selector = PathProximalSelector(args.target_file, args.func)
    
    # Retrieve target skeleton for display
    skeleton = selector.get_structural_skeleton(args.line)
    print(f"[+] Target path skeleton line numbers: {sorted(list(skeleton))}")

    # Execute hierarchical search algorithm
    result = selector.select_best_test(unit, traces)

    if result:
        test_id, score = result
        covered_lines = sorted(list(traces[test_id].covered_lines))
        print("\n" + "="*30)
        print(f"Result: Closest test case found")
        print(f"Test ID      : {test_id}")
        print(f"Similarity   : {score:.4f}")
        print(f"Covered lines: {len(covered_lines)}")
        print(f"Line numbers : {covered_lines}")
        print("="*30)
    else:
        print("\n[-] No related test case could be found.")

if __name__ == "__main__":
    main()