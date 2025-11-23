import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -4179
            list_0 = []
            int_1 = -654
            int_2 = -2153
            token_0 = module_0.Token(int_0, int_1, int_2)
            token_1 = token_0.lookup_key(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
