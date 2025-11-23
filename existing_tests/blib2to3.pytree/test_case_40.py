import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            int_0 = 92
            str_0 = '3-K!`DrxuvP^'
            leaf_0 = module_0.Leaf(int_0, str_0)
            leaf_1 = leaf_0.clone()
            str_1 = leaf_0.__repr__()
            leaf_2 = leaf_0.clone()
            wildcard_pattern_0 = module_0.WildcardPattern()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
