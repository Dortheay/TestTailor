import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            grammar_0 = module_1.Grammar()
            node_pattern_0 = module_0.NodePattern()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
