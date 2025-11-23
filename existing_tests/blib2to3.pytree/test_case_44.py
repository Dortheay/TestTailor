import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        try:
            str_0 = 'PtternGramm6ar.txt'
            int_0 = 63
            leaf_0 = module_0.Leaf(int_0, str_0)
            leaf_1 = leaf_0.clone()
            leaf_2 = leaf_1.clone()
            int_1 = 4161
            list_0 = []
            node_0 = module_0.Node(int_1, list_0)
            node_0.append_child(leaf_2)
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            base_0 = module_0.Base()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
