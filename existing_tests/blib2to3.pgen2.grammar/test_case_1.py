import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0

class Test_Grammar_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'JfLZ?v'
        grammar_0 = module_0.Grammar()
        grammar_0.dump(str_0)

if __name__ == "__main__":
    unittest.main()
