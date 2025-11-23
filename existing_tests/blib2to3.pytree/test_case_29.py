import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            int_0 = 42
            int_1 = 1351
            str_0 = 'w\x0bkDon2EcvOu'
            leaf_0 = module_0.Leaf(int_0, str_0)
            list_0 = [leaf_0]
            wildcard_pattern_0 = module_0.WildcardPattern(str_0)
            any_0 = wildcard_pattern_0.optimize()
            dict_0 = {}
            node_0 = module_0.Node(int_1, list_0, any_0, dict_0)
            node_1 = node_0.clone()
            node_2 = node_1.clone()
            node_pattern_0 = module_0.NodePattern(int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
