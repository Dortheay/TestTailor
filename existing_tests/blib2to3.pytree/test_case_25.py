import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            none_type_0 = None
            str_0 = '\n        The whitespace and comments preceding this token in the input.\n        '
            leaf_pattern_0 = module_0.LeafPattern(none_type_0, str_0)
            int_0 = 19
            leaf_0 = None
            var_0 = leaf_pattern_0.match(leaf_0)
            str_1 = '$'
            wildcard_pattern_0 = module_0.WildcardPattern(str_1, int_0)
            any_0 = wildcard_pattern_0.optimize()
            any_1 = wildcard_pattern_0.optimize()
            negated_pattern_0 = module_0.NegatedPattern(any_1)
            bool_0 = wildcard_pattern_0.match_seq(negated_pattern_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
