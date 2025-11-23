import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0

class Test_Grammar_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        grammar_0 = module_0.Grammar()
        grammar_0.report()
        grammar_1 = module_0.Grammar()
        var_0 = grammar_1.copy()
        var_1 = grammar_1.copy()

if __name__ == "__main__":
    unittest.main()
