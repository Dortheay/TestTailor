import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            int_0 = 17
            int_1 = 548
            leaf_0 = None
            list_0 = [leaf_0, leaf_0]
            str_0 = '`b<=\nv\x0c\'bkU"ldZx~t'
            var_0 = None
            list_1 = [int_0, var_0]
            node_0 = module_0.Node(int_1, list_0, str_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
