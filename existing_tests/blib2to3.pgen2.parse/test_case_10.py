import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'if'
            str_1 = 'else'
            int_0 = 1
            int_1 = 1195
            int_2 = -1393
            tuple_0 = (int_1, int_2)
            tuple_1 = (str_1, tuple_0)
            grammar_0 = module_0.Grammar()
            parser_0 = module_1.Parser(grammar_0)
            bool_0 = parser_0.addtoken(int_0, str_0, tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
