import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -3502
            str_0 = "'''"
            int_1 = None
            int_2 = -424
            tuple_0 = (int_2, int_2)
            tuple_1 = (str_0, tuple_0)
            grammar_0 = module_0.Grammar()
            parser_0 = module_1.Parser(grammar_0)
            parser_0.shift(int_0, str_0, int_1, tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
