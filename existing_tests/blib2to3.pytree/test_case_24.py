import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            leaf_pattern_0 = module_0.LeafPattern()
            list_0 = [leaf_pattern_0, leaf_pattern_0]
            base_pattern_0 = module_0.BasePattern(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
