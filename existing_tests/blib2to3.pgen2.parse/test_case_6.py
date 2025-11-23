import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            grammar_0 = module_0.Grammar()
            parser_0 = module_1.Parser(grammar_0)
            tuple_0 = None
            grammar_1 = module_0.Grammar()
            parser_1 = module_1.Parser(grammar_1)
            int_0 = None
            tuple_1 = None
            int_1 = -2944
            parser_0.push(int_0, tuple_1, int_1, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
