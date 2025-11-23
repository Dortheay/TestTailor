import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 1255
            list_0 = []
            dict_0 = {int_0: int_0}
            list_1 = [dict_0, dict_0, list_0]
            list_2 = [int_0, list_0]
            node_0 = module_0.Node(int_0, list_0, list_1, list_2)
            node_1 = node_0.clone()
            negated_pattern_0 = module_0.NegatedPattern(node_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
