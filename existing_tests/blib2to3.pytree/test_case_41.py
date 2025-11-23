import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            int_0 = 42
            int_1 = 1351
            str_0 = 'T\\m\x0cwz[ae2\x0b"!r{i,'
            leaf_0 = module_0.Leaf(int_0, str_0)
            list_0 = [leaf_0]
            dict_0 = {str_0: leaf_0}
            node_0 = module_0.Node(int_1, list_0, str_0, dict_0)
            node_1 = node_0.clone()
            list_1 = [node_1]
            node_2 = module_0.Node(int_0, list_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
