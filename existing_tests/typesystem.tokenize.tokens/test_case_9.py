import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'M%Mmg\\\x0c9 S\x0bEJ/A_N\\W'
        int_0 = 1761
        scalar_token_0 = module_0.ScalarToken(str_0, int_0, int_0)

if __name__ == "__main__":
    unittest.main()
