import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            int_0 = 5
            int_1 = 19
            str_0 = '0Ga~\rNzF,8mJ$]a7fu#/'
            str_1 = '~N$_}S$R#+d_N0'
            int_2 = 361
            int_3 = -1809
            tuple_0 = (int_2, int_3)
            tuple_1 = (str_1, tuple_0)
            list_0 = [str_0]
            leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, list_0)
            leaf_1 = leaf_0.clone()
            list_1 = [leaf_1, leaf_0, leaf_0, leaf_1]
            node_0 = module_0.Node(int_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
