import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            int_0 = 2882
            int_1 = 1197
            list_0 = []
            node_0 = module_0.Node(int_1, list_0)
            list_1 = [node_0, node_0]
            node_1 = module_0.Node(int_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
