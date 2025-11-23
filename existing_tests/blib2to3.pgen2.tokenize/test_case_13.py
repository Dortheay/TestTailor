import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = -1835
            int_1 = 593
            tuple_0 = (int_0, int_1)
            token_error_0 = module_0.TokenError()
            set_0 = set()
            str_0 = 'U'
            list_0 = [token_error_0, tuple_0]
            grammar_0 = module_1.Grammar()
            var_0 = grammar_0.copy()
            var_1 = module_0.printtoken(set_0, str_0, list_0, int_1, var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
