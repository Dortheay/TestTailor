import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_28(self):
        try:
            int_0 = 59
            str_0 = '3-K!`DrxuvP^'
            leaf_0 = module_0.Leaf(int_0, str_0)
            leaf_1 = leaf_0.clone()
            leaf_2 = leaf_1.clone()
            leaf_3 = leaf_2.clone()
            str_1 = leaf_3.__str__()
            leaf_4 = leaf_3.clone()
            leaf_5 = leaf_4.clone()
            leaf_6 = leaf_5.clone()
            leaf_7 = leaf_6.clone()
            int_1 = -1350
            list_0 = [leaf_7, leaf_1]
            list_1 = [int_0, int_0, leaf_5, str_0]
            node_0 = module_0.Node(int_1, list_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
