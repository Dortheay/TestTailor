import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            grammar_0 = module_1.Grammar()
            var_0 = grammar_0.copy()
            list_0 = [grammar_0, grammar_0]
            str_0 = module_0.untokenize(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
