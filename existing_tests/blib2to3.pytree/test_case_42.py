import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        try:
            leaf_pattern_0 = module_0.LeafPattern()
            grammar_0 = module_1.Grammar()
            str_0 = 'Y'
            negated_pattern_0 = module_0.NegatedPattern()
            bool_0 = negated_pattern_0.match_seq(str_0)
            int_0 = 225
            var_0 = module_0.type_repr(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
