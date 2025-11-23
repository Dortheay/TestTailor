import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = None
            str_0 = ''
            tuple_0 = None
            grammar_0 = module_0.Grammar()
            parser_0 = module_1.Parser(grammar_0)
            int_1 = parser_0.classify(int_0, str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
