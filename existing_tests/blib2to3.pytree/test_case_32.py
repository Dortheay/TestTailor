import unittest
import timeout_decorator
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Pytree_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            int_0 = 19
            str_0 = '0Ga~\rNzF,8mJ$]a7fu#/'
            int_1 = -1428
            wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
