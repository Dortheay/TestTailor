import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            list_0 = None
            str_0 = '#Pss{D% S/:Gz'
            dict_0 = {str_0: str_0}
            list_1 = [dict_0]
            int_0 = -3515
            token_0 = module_0.Token(list_1, int_0, int_0, str_0)
            token_1 = token_0.lookup_key(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
