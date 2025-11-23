import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            wildcard_pattern_0 = module_0.WildcardPattern()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
