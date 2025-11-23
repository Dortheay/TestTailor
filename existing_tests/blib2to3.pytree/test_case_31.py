import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            int_0 = 59
            str_0 = '3-K!`DrxuvP^'
            leaf_0 = module_0.Leaf(int_0, str_0)
            leaf_1 = leaf_0.clone()
            int_1 = -2028
            wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
