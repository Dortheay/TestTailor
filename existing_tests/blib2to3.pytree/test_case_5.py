import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = '$'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()

if __name__ == "__main__":
    unittest.main()
