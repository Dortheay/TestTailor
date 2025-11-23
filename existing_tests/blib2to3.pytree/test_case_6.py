import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '0Ga~\rNzF,mJ$]a7fu#/'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()
        int_0 = 59
        wildcard_pattern_1 = module_0.WildcardPattern(str_0, int_0)
        any_1 = wildcard_pattern_1.optimize()

if __name__ == "__main__":
    unittest.main()
