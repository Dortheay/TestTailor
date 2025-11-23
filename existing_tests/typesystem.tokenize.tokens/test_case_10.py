import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        list_0 = []
        str_0 = '+dM*$b2s_\ng%[+8\t'
        str_1 = '7DHC\rN'
        list_1 = [str_1, str_1, str_1]
        dict_0 = {str_0: str_0, str_0: str_0, str_1: list_1, str_1: list_1}
        int_0 = -1073
        int_1 = 994
        token_0 = module_0.Token(dict_0, int_0, int_1)
        token_1 = token_0.lookup(list_0)

if __name__ == "__main__":
    unittest.main()
