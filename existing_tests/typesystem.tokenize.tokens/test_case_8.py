import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            list_0 = []
            int_0 = 4
            str_0 = '+d0 *'
            token_0 = module_0.Token(list_0, int_0, int_0, str_0)
            bool_0 = token_0.__eq__(list_0)
            int_1 = 2
            scalar_token_0 = module_0.ScalarToken(token_0, int_1, int_1, str_0)
            token_1 = token_0.lookup(list_0)
            bool_1 = token_0.__eq__(scalar_token_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
