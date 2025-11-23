import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

class Test_Parse_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            grammar_0 = module_0.Grammar()
            parser_0 = module_1.Parser(grammar_0)
            int_0 = -1941
            parser_0.setup(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
