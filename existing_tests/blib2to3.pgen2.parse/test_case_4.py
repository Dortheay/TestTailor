import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = ''
            tuple_0 = None
            int_0 = 2387
            grammar_0 = module_0.Grammar()
            parser_0 = module_1.Parser(grammar_0)
            bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
