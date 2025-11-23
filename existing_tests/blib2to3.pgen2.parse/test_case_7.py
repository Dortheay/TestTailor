import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = "w'/QvVV/T\\atT*g[kD"
            int_0 = 17
            tuple_0 = (int_0, int_0)
            tuple_1 = (str_0, tuple_0)
            grammar_0 = module_0.Grammar()
            str_1 = '6hu~T_#Cz,B'
            parser_0 = module_1.Parser(grammar_0, str_1)
            bool_0 = parser_0.addtoken(int_0, str_0, tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
