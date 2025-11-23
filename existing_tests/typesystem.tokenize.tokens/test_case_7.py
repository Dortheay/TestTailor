import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            scalar_token_0 = None
            int_0 = 53
            str_0 = 'invalid_key'
            list_token_0 = module_0.ListToken(scalar_token_0, int_0, int_0, str_0)
            int_1 = -1942
            list_0 = [scalar_token_0, int_1, int_0]
            list_1 = [scalar_token_0, int_1]
            token_0 = module_0.Token(int_1, int_0, int_1, str_0)
            list_2 = [list_1, int_0, list_0, list_token_0]
            dict_token_0 = module_0.DictToken(*list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
