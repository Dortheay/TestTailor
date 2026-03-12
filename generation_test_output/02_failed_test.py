import sys
import unittest
import timeout_decorator
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "tests"))

from sample_target_v2 import nested_branch


# LLM forgot the colon after class definition  ← intentional compile error
class Test(unittest.TestCase)
    @timeout_decorator.timeout(1)
    def test_case_XX(self):
        """complete the test case here"""
        result = nested_branch(12)
        self.assertEqual(result, "big even")
