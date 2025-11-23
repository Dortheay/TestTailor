import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0

class Test_Tokenize_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        untokenizer_0 = module_0.Untokenizer()

if __name__ == "__main__":
    unittest.main()
