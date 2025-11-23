import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            int_0 = -5
            str_0 = "#:7cb '"
            leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
