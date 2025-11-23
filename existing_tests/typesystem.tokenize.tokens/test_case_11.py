import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        scalar_token_0 = None
        int_0 = 53
        str_0 = 'invalid_key'
        list_token_0 = module_0.ListToken(scalar_token_0, int_0, int_0, str_0)
        int_1 = -1942
        str_1 = '\x0c`}\x0cA'
        scalar_token_1 = module_0.ScalarToken(scalar_token_0, int_1, int_1, str_1)
        int_2 = 1752
        token_0 = module_0.Token(scalar_token_1, int_1, int_2)
        bool_0 = token_0.__eq__(str_1)
        list_token_1 = module_0.ListToken(scalar_token_1, int_1, int_1)

if __name__ == "__main__":
    unittest.main()
