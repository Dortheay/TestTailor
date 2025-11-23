import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            pgen_grammar_0 = module_0.generate_grammar()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
