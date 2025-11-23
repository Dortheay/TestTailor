import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        none_type_0 = None
        str_0 = '\x0c        The whitespace a\rd comments preceding this token in the input.\n        '
        leaf_pattern_0 = module_0.LeafPattern(none_type_0, str_0)
        node_0 = None
        grammar_0 = module_1.Grammar()
        negated_pattern_0 = module_0.NegatedPattern()
        bool_0 = negated_pattern_0.match(node_0, grammar_0)

if __name__ == "__main__":
    unittest.main()
