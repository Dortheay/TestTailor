import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        node_0 = None
        leaf_pattern_0 = module_0.LeafPattern()
        var_0 = leaf_pattern_0.match(node_0)

if __name__ == "__main__":
    unittest.main()
