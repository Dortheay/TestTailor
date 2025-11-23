import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_44(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            int_0 = 42
            int_1 = 1351
            str_0 = 'T\\m\x0cwz[ae2\x0b"!r{i,'
            leaf_0 = module_0.Leaf(int_0, str_0)
            list_0 = [leaf_0]
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            any_0 = wildcard_pattern_0.optimize()
            dict_0 = {str_0: leaf_0}
            node_0 = module_0.Node(int_1, list_0, any_0, dict_0)
            node_1 = node_0.clone()
            node_2 = node_1.clone()
            any_1 = wildcard_pattern_0.optimize()
            leaf_pattern_0 = module_0.LeafPattern(int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
