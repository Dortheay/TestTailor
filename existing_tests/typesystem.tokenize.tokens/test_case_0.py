import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            list_0 = [dict_0, dict_0, dict_0]
            dict_1 = None
            tuple_0 = (dict_1,)
            int_0 = 3147
            str_0 = '6$ezr2E$0'
            token_0 = module_0.Token(tuple_0, int_0, int_0, str_0)
            token_1 = token_0.lookup(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
