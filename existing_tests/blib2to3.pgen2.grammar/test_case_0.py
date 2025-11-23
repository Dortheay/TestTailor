import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0

class Test_Grammar_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        grammar_0 = module_0.Grammar()

if __name__ == "__main__":
    unittest.main()
