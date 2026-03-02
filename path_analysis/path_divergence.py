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

import ast
from typing import List, Optional, Set, Tuple

from models import (
    CodeUnit, ExecutionPath, PathProximalTest, TargetPath
)


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _common_prefix(a: List[int], b: List[int]) -> List[int]:
    prefix = []
    for x, y in zip(a, b):
        if x == y:
            prefix.append(x)
        else:
            break
    return prefix


def _lines_around(source_lines: List[str], lineno: int, context: int = 2) -> str:
    """Extract a few lines around *lineno* for display."""
    start = max(0, lineno - 1 - context)
    end = min(len(source_lines), lineno + context)
    snippet_lines = []
    for i, line in enumerate(source_lines[start:end], start=start + 1):
        marker = ">>>" if i == lineno else "   "
        snippet_lines.append(f"{marker} {i:4d}: {line.rstrip()}")
    return "\n".join(snippet_lines)


# ──────────────────────────────────────────────────────────────────────────────
# Divergence Analyzer
# ──────────────────────────────────────────────────────────────────────────────

class PathDivergenceAnalyzer:
    """
    Compares the execution path of a path-proximal test against the target
    path to locate the first divergence point.
    """

    def __init__(self, source: str):
        self.source = source
        self.source_lines = source.splitlines()
        self.tree = ast.parse(source)

    def analyze(
        self,
        proximal: PathProximalTest,
        target_path: TargetPath,
    ) -> PathProximalTest:
        """
        Annotate *proximal* with divergence information and return it.
        """
        target_seq = target_path.path_nodes          # ordered decision lines
        proximal_seq = proximal.execution_path.visited_nodes  # actual trace

        div_lineno, div_condition = self._find_divergence(target_seq, proximal_seq)

        if div_lineno is not None:
            proximal.divergence_lineno = div_lineno
            proximal.divergence_condition = div_condition
            proximal.target_continues_to = self._what_target_does_next(
                target_seq, div_lineno
            )
            proximal.proximal_continues_to = self._what_proximal_does_next(
                proximal_seq, div_lineno
            )
        else:
            # No divergence found in structural path – the test may reach the
            # function but miss the unit for a different reason (e.g., the
            # unit's lines are inside a loop iteration that isn't reached).
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
    ) -> Tuple[Optional[int], Optional[str]]:
        """
        Walk both sequences in parallel and return (lineno, condition_text) at
        the first point they differ.

        Strategy
        --------
        We align on the *common prefix* (identical line numbers in order),
        then the first element that appears in target_seq but NOT in the
        proximal's subsequent visited lines is the divergence point.
        """
        proximal_set = set(proximal_seq)
        target_set = set(target_seq)

        # The divergence is the first target node not covered by the proximal
        for lineno in target_seq:
            if lineno not in proximal_set:
                cond = self._get_condition_at_line(lineno)
                return lineno, cond

        # All target nodes are covered – divergence is at the unit itself
        return None, None

    def _get_condition_at_line(self, lineno: int) -> str:
        """Return the source text (condition or statement) at *lineno*."""
        for node in ast.walk(self.tree):
            if getattr(node, 'lineno', None) == lineno:
                try:
                    return ast.unparse(node)
                except Exception:
                    pass
        # Fallback to raw source line
        if 0 < lineno <= len(self.source_lines):
            return self.source_lines[lineno - 1].strip()
        return f"line {lineno}"

    def _what_target_does_next(
        self,
        target_seq: List[int],
        after_lineno: int,
    ) -> str:
        """Return what the target path does after the divergence point."""
        try:
            idx = target_seq.index(after_lineno)
            if idx + 1 < len(target_seq):
                next_line = target_seq[idx + 1]
                return self._get_condition_at_line(next_line)
        except ValueError:
            pass
        return f"(continues toward target unit)"

    def _what_proximal_does_next(
        self,
        proximal_seq: List[int],
        after_lineno: int,
    ) -> str:
        """Return what the proximal test actually does instead."""
        # Find after_lineno in the proximal sequence, then return next
        for i, ln in enumerate(proximal_seq):
            if ln == after_lineno and i + 1 < len(proximal_seq):
                next_line = proximal_seq[i + 1]
                return self._get_condition_at_line(next_line)
        return "(different branch or skips entirely)"


# ──────────────────────────────────────────────────────────────────────────────
# Divergence → prompt text
# ──────────────────────────────────────────────────────────────────────────────

def format_divergence(proximal: PathProximalTest) -> str:
    """Render the divergence info as a human-readable block for the LLM prompt."""
    lines = ["Path Divergence Analysis"]
    lines.append("-" * 40)

    if proximal.divergence_lineno:
        lines.append(
            f"The existing test case diverges at:\n"
            f"    {proximal.divergence_condition} "
            f"(line {proximal.divergence_lineno})"
        )
    else:
        lines.append(
            f"The existing test case diverges at:\n"
            f"    {proximal.divergence_condition}"
        )

    lines.append(
        f"\nTarget path continues to:\n    {proximal.target_continues_to}"
    )
    lines.append(
        f"\nExisting test path continues to:\n    {proximal.proximal_continues_to}"
    )
    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Convenience entry point
# ──────────────────────────────────────────────────────────────────────────────

def analyze_divergence(
    proximal: PathProximalTest,
    target_path: TargetPath,
    source: str,
) -> PathProximalTest:
    """High-level entry point."""
    analyzer = PathDivergenceAnalyzer(source)
    return analyzer.analyze(proximal, target_path)
