import sys
import unittest
from pathlib import Path

# Make sample_target_v2 importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from sample_target_v2 import nested_branch


class TestNestedBranchSmall(unittest.TestCase):
    """Covers only the 'small' (n <= 10) branch."""

    def test_small_value(self):
        self.assertEqual(nested_branch(5), "small")

    def test_boundary_small(self):
        self.assertEqual(nested_branch(10), "small")


if __name__ == "__main__":
    unittest.main()
