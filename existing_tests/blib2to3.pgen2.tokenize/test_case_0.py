import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0

class Test_Tokenize_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        token_error_0 = module_0.TokenError()

if __name__ == "__main__":
    unittest.main()
