"""
Path Divergence Analyzer
=========================
Given a PathProximalTest and a TargetPath, find the first divergence point:
the specific branch/statement where the proximal test's actual execution
deviates from the intended target path.

The output is embedded into the LLM prompt as:
    "The existing test case diverges at: <condition>
     Target path continues to: <what should happen>
     Existing test path continues to: <what actually happened>"
"""

import argparse
import ast
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from models import CodeUnit, ExecutionPath, PathProximalTest, TargetPath
from path_analysis.cfg_builder import build_cfg_from_file, CFG
from path_analysis.symbolic_executor import SymbolicConstraintExtractor
from execution.trace_collector import collect_test_suite_traces


# ──────────────────────────────────────────────────────────────────────────────
# Divergence Analyzer
# ──────────────────────────────────────────────────────────────────────────────

class PathDivergenceAnalyzer:
    """
    Compares the execution path of a path-proximal test against the target
    path to locate the first divergence point.

    Algorithm
    ---------
    Walk *target_path.path_nodes* in order.  For each mandatory node:
      - If the proximal trace covers it → mark it as the *last shared node*.
      - If the proximal trace does NOT cover it → this is the divergence point.

    The output answers three questions:
      1. Where does the path diverge?  (divergence_lineno / divergence_condition)
      2. What does the target path do next?  (target_continues_to)
      3. What does the proximal test do instead?  (proximal_continues_to)
    """

    def __init__(self, source: str):
        self.source = source
        self.source_lines = source.splitlines()
        self.tree = ast.parse(source)
        # CFG node-type lookup built on demand (branch / loop_header labelling)
        self._lineno_to_node_type: Dict[int, str] = {}

    # ── Public API ───────────────────────────────────────────────────────────

    def load_cfg(self, source_file: str, function_name: str) -> None:
        """
        Optionally load the CFG for the target function so that divergence
        conditions can be prefixed with their structural type
        (e.g. "[branch]", "[loop]").
        """
        try:
            cfg, _ = build_cfg_from_file(source_file, function_name)
            for node in cfg.nodes.values():
                if node.lineno is not None:
                    self._lineno_to_node_type[node.lineno] = node.node_type
        except Exception:
            pass  # CFG enrichment is optional; AST-only fallback is fine

    def analyze(
        self,
        proximal: PathProximalTest,
        target_path: TargetPath,
    ) -> PathProximalTest:
        """
        Annotate *proximal* with divergence information and return it.
        """
        # Load CFG for richer node labels when source_file is available
        unit = target_path.unit
        if unit.source_file and unit.function_name:
            self.load_cfg(unit.source_file, unit.function_name)

        target_seq = target_path.path_nodes           # ordered decision linenos
        proximal_seq = proximal.execution_path.visited_nodes  # runtime trace

        div_lineno, div_condition, last_shared = self._find_divergence(
            target_seq, proximal_seq
        )

        if div_lineno is not None:
            proximal.divergence_lineno = div_lineno
            proximal.divergence_condition = div_condition
            proximal.target_continues_to = self._what_target_does_next(
                target_seq, div_lineno
            )
            proximal.proximal_continues_to = self._what_proximal_does_next(
                proximal_seq, last_shared
            )
        else:
            # All target nodes are covered but the unit is still not reached
            # (e.g. the relevant loop iteration is never executed).
            proximal.divergence_condition = "(could not pinpoint divergence)"
            proximal.target_continues_to = (
                f"line {target_path.unit.start_lineno} (target unit)"
            )
            proximal.proximal_continues_to = "(test did not reach this line)"

        return proximal

    # ── Internals ────────────────────────────────────────────────────────────

    def _find_divergence(
        self,
        target_seq: List[int],
        proximal_seq: List[int],
    ) -> Tuple[Optional[int], Optional[str], Optional[int]]:
        """
        Walk *target_seq* in order and return
        ``(div_lineno, condition_text, last_shared_lineno)``.

        *last_shared_lineno* is the last target-path node that the proximal
        trace DID cover; it is used by ``_what_proximal_does_next`` to find
        what the proximal test executes instead of going to the divergence point.
        """
        proximal_covered = set(proximal_seq)
        last_shared: Optional[int] = None

        for lineno in target_seq:
            if lineno in proximal_covered:
                last_shared = lineno
            else:
                cond = self._get_condition_at_line(lineno)
                return lineno, cond, last_shared

        # All target nodes are covered – no structural divergence found
        return None, None, last_shared

    def _get_condition_at_line(self, lineno: int) -> str:
        """
        Return a concise description of the condition / statement at *lineno*.

        For control-flow nodes (if / for / while) only the predicate is shown,
        not the body.  An optional CFG-type prefix ("[branch]", "[loop]") is
        prepended when the CFG has been loaded.
        """
        node_type = self._lineno_to_node_type.get(lineno, "")
        prefix = ""
        if node_type == "branch":
            prefix = "[branch] "
        elif node_type == "loop_header":
            prefix = "[loop] "

        for node in ast.walk(self.tree):
            if getattr(node, "lineno", None) != lineno:
                continue
            try:
                if isinstance(node, ast.If):
                    return f"{prefix}if {ast.unparse(node.test)}"
                if isinstance(node, (ast.For, ast.AsyncFor)):
                    return (
                        f"{prefix}for {ast.unparse(node.target)}"
                        f" in {ast.unparse(node.iter)}"
                    )
                if isinstance(node, ast.While):
                    return f"{prefix}while {ast.unparse(node.test)}"
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    args = ast.unparse(node.args)
                    return f"{prefix}def {node.name}({args}):"
                if isinstance(node, ast.ClassDef):
                    return f"{prefix}class {node.name}:"
                if isinstance(node, ast.Try):
                    return f"{prefix}try: ..."
                return f"{prefix}{ast.unparse(node)}"
            except Exception:
                pass

        # Fallback: raw source line
        if 0 < lineno <= len(self.source_lines):
            return f"{prefix}{self.source_lines[lineno - 1].strip()}"
        return f"line {lineno}"

    def _what_target_does_next(
        self,
        target_seq: List[int],
        after_lineno: int,
    ) -> str:
        """Return what the target path expects to happen after *after_lineno*."""
        try:
            idx = target_seq.index(after_lineno)
            if idx + 1 < len(target_seq):
                return self._get_condition_at_line(target_seq[idx + 1])
        except ValueError:
            pass
        return "(continues toward target unit)"

    def _what_proximal_does_next(
        self,
        proximal_seq: List[int],
        after_lineno: Optional[int],
    ) -> str:
        """
        Return what the proximal test actually executes after the last node it
        shares with the target path (*after_lineno* = last_shared_lineno).

        We look for the *last* occurrence of *after_lineno* in the trace (to
        handle loops where the same line may appear multiple times) and then
        return the immediately following line.
        """
        if after_lineno is None:
            # Proximal trace shares no target-path node at all
            if proximal_seq:
                return self._get_condition_at_line(proximal_seq[0])
            return "(different branch or skips entirely)"

        # Find the last occurrence of after_lineno in the proximal trace
        last_idx: Optional[int] = None
        for i, ln in enumerate(proximal_seq):
            if ln == after_lineno:
                last_idx = i

        if last_idx is not None and last_idx + 1 < len(proximal_seq):
            return self._get_condition_at_line(proximal_seq[last_idx + 1])

        return "(different branch or skips entirely)"


# ──────────────────────────────────────────────────────────────────────────────
# Divergence → prompt text
# ──────────────────────────────────────────────────────────────────────────────

def format_divergence(proximal: PathProximalTest) -> str:
    """Render the divergence info as the three-line block used in the LLM prompt."""
    if proximal.divergence_lineno:
        div_at = (
            f"{proximal.divergence_condition} (line {proximal.divergence_lineno})"
        )
    else:
        div_at = proximal.divergence_condition or "(could not pinpoint divergence)"

    return (
        f"The existing test case diverges from the target path at:  {div_at}\n"
        f"Target path continues to:  {proximal.target_continues_to}\n"
        f"But existing test path continues to: {proximal.proximal_continues_to}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# Convenience entry point
# ──────────────────────────────────────────────────────────────────────────────

def analyze_divergence(
    proximal: PathProximalTest,
    target_path: TargetPath,
    source: str,
) -> PathProximalTest:
    """High-level entry point used by the pipeline."""
    analyzer = PathDivergenceAnalyzer(source)
    return analyzer.analyze(proximal, target_path)


# ──────────────────────────────────────────────────────────────────────────────
# CLI / main
# ──────────────────────────────────────────────────────────────────────────────

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Locate the first divergence point between a path-proximal test's "
            "execution trace and the target path to a CodeUnit."
        )
    )
    parser.add_argument(
        "--target-file",
        required=True,
        help="Path to the Python source file containing the target function.",
    )
    parser.add_argument(
        "--func",
        required=True,
        help="Name of the target function.",
    )
    parser.add_argument(
        "--line",
        type=int,
        required=True,
        help="Start line number of the uncovered target CodeUnit.",
    )
    parser.add_argument(
        "--tests-dir",
        required=True,
        help="Directory containing existing test_*.py files.",
    )
    return parser.parse_args()


def main() -> None:
    """
    End-to-end CLI for manual testing of the divergence analysis pipeline.

    Steps performed
    ---------------
    1. Read the target source file.
    2. Build a TargetPath (with path_nodes + constraints) via SymbolicConstraintExtractor.
    3. Collect runtime execution traces from all test_*.py files in --tests-dir.
    4. Select the path-proximal test via PathProximalSelector.
    5. Run PathDivergenceAnalyzer and print the result.

    Example
    -------
        python -m path_analysis.path_divergence \\
            --target-file tests/sample_target_v2.py \\
            --func mixed_constructs \\
            --line 33 \\
            --tests-dir tests/order_management/tests/
    """
    args = _parse_args()

    # ── 1. Read source ────────────────────────────────────────────────────────
    target_file = os.path.realpath(args.target_file)
    source = Path(target_file).read_text(encoding="utf-8")

    # ── 2. Build CodeUnit + TargetPath ────────────────────────────────────────
    unit = CodeUnit(
        unit_id=f"{args.func}:{args.line}",
        source_file=target_file,
        function_name=args.func,
        start_lineno=args.line,
        end_lineno=args.line,
        unit_type="linear",
        code_snippet="",
    )
    extractor = SymbolicConstraintExtractor(source)
    target_path = extractor.extract(unit)

    print(f"[*] Target path nodes : {target_path.path_nodes}")
    print(f"[*] Path constraints  : {[c.condition for c in target_path.constraints]}")

    # ── 3. Collect execution traces ───────────────────────────────────────────
    tests_dir = Path(args.tests_dir)
    test_sources: Dict[str, str] = {
        p.stem: p.read_text(encoding="utf-8")
        for p in tests_dir.glob("test_*.py")
    }
    if not test_sources:
        print(f"[-] No test_*.py files found in {args.tests_dir}")
        return

    print(f"\n[*] Collecting traces for {len(test_sources)} test file(s)...")
    traces = collect_test_suite_traces(test_sources, target_file)

    # ── 4. Select path-proximal test ──────────────────────────────────────────
    from path_analysis.path_proximal import PathProximalSelector

    selector = PathProximalSelector(target_file, args.func)
    result = selector.select_best_test(unit, traces)

    if result is None:
        print("[-] No path-proximal test found.")
        return

    best_id, score = result
    best_trace = traces[best_id]
    proximal = PathProximalTest(
        test_id=best_id,
        test_source=best_trace.test_source,
        execution_path=best_trace,
        jaccard_similarity=score,
    )

    # ── 5. Analyze divergence ─────────────────────────────────────────────────
    analyzer = PathDivergenceAnalyzer(source)
    proximal = analyzer.analyze(proximal, target_path)

    # ── 6. Display results ────────────────────────────────────────────────────
    print("\n" + "=" * 55)
    print(
        f"Path-Proximal Test : {proximal.test_id}"
        f"  (Jaccard: {proximal.jaccard_similarity:.4f})"
    )
    print("=" * 55)
    print(format_divergence(proximal))
    print("=" * 55)


if __name__ == "__main__":
    main()
