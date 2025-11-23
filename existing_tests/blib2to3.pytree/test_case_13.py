import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 59
            str_0 = '3-K!`DrxuvP^'
            leaf_0 = module_0.Leaf(int_0, str_0)
            leaf_1 = leaf_0.clone()
            wildcard_pattern_0 = module_0.WildcardPattern()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
