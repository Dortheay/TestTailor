import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = 19
        str_0 = '$'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        leaf_pattern_0 = module_0.LeafPattern(int_0)
        negated_pattern_0 = module_0.NegatedPattern()

if __name__ == "__main__":
    unittest.main()
