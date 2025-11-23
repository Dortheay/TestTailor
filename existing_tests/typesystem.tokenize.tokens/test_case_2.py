import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            int_0 = 5
            str_0 = 'C31s'
            token_0 = module_0.Token(bool_0, int_0, int_0, str_0)
            str_1 = token_0.__repr__()
            str_2 = token_0.__repr__()
            dict_token_0 = module_0.DictToken()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
