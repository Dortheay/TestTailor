import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0

class Test_Grammar_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        grammar_0 = module_0.Grammar()
        var_0 = grammar_0.copy()

if __name__ == "__main__":
    unittest.main()
