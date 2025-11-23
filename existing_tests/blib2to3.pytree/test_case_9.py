import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        int_0 = 1197
        list_0 = []
        node_0 = module_0.Node(int_0, list_0)
        str_0 = node_0.__str__()

if __name__ == "__main__":
    unittest.main()
