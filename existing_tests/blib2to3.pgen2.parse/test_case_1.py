import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            grammar_0 = module_0.Grammar()
            int_0 = -2997
            str_0 = 'OBb1D9D'
            int_1 = 47
            int_2 = 4158
            tuple_0 = (int_1, int_2)
            tuple_1 = (str_0, tuple_0)
            float_0 = -494.7153
            tuple_2 = (int_0, str_0, tuple_1, float_0)
            var_0 = module_1.lam_sub(grammar_0, tuple_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
