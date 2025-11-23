import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '0Ga~\rNzF,8mJ$]a7fu#/'
        wildcard_pattern_0 = module_0.WildcardPattern(str_0)
        any_0 = wildcard_pattern_0.optimize()

if __name__ == "__main__":
    unittest.main()
