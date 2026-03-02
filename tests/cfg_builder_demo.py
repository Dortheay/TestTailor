import os
import sys
from pathlib import Path


# Ensure project root is on sys.path so we can import path_analysis.cfg_builder
HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from path_analysis.cfg_builder import build_cfg_from_file, _format_cfg_for_cli  # type: ignore


def run_demo() -> None:
    """
    Simple, self-contained demo for the CFG builder.

    It analyzes a few sample functions from tests/sample_target.py and
    tests/sample_target_v2.py and prints their CFGs to stdout.
    """
    targets = [
        (PROJECT_ROOT / "tests" / "sample_target.py", "simple_function"),
        (PROJECT_ROOT / "tests" / "sample_target.py", "conditional_function"),
        (PROJECT_ROOT / "tests" / "sample_target.py", "loop_function"),
        (PROJECT_ROOT / "tests" / "sample_target_v2.py", "compute"),
        (PROJECT_ROOT / "tests" / "sample_target_v2.py", "nested_branch"),
        (PROJECT_ROOT / "tests" / "sample_target_v2.py", "mixed_constructs"),
    ]

    for path, func in targets:
        if not path.exists():
            continue
        print("=" * 80)
        print(f"CFG for {func} in {os.path.relpath(path, PROJECT_ROOT)}")
        print("-" * 80)
        cfg, dom = build_cfg_from_file(str(path), func)
        print(_format_cfg_for_cli(cfg, dom))
        print()  # blank line between functions


if __name__ == "__main__":
    run_demo()

