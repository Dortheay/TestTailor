import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            int_0 = 5
            list_0 = []
            wildcard_pattern_0 = module_0.WildcardPattern(list_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
