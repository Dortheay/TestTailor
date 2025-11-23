import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -807
            list_0 = []
            node_0 = module_0.Node(int_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
