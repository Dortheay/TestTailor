import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 0
            list_0 = [int_0]
            float_0 = 784.207
            dict_0 = {float_0: float_0, float_0: float_0}
            int_1 = 184
            int_2 = 6
            list_token_0 = module_0.ListToken(dict_0, int_1, int_2)
            scalar_token_0 = module_0.ScalarToken(list_token_0, int_1, int_2)
            int_3 = 2171
            token_0 = module_0.Token(scalar_token_0, int_1, int_3)
            token_1 = token_0.lookup_key(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
