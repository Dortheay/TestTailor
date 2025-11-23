import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            int_0 = 3640
            list_0 = []
            list_1 = [list_0]
            node_0 = module_0.Node(int_0, list_0, list_1)
            node_1 = node_0.clone()
            node_2 = node_1.clone()
            node_3 = node_2.clone()
            node_4 = node_3.clone()
            node_4.update_sibling_maps()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
