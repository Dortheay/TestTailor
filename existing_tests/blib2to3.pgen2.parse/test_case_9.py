import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 48
            str_0 = None
            grammar_0 = module_0.Grammar()
            str_1 = 'RY\x0b:u9HH'
            tuple_0 = (int_0, int_0)
            tuple_1 = (str_1, tuple_0)
            optional_0 = None
            tuple_2 = (int_0, str_0, tuple_1, optional_0)
            var_0 = module_1.lam_sub(grammar_0, tuple_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
