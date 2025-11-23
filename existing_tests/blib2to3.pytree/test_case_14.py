import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 59
            str_0 = '3-K!`DrxuvP^'
            leaf_0 = module_0.Leaf(int_0, str_0)
            leaf_1 = leaf_0.clone()
            str_1 = leaf_0.__repr__()
            leaf_2 = leaf_0.clone()
            leaf_3 = leaf_0.clone()
            grammar_0 = module_1.Grammar()
            list_0 = [leaf_0, leaf_3]
            tuple_0 = (int_0, str_0, leaf_2, list_0)
            var_0 = module_0.convert(grammar_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
