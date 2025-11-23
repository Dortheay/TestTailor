import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '#+B7bTQ6\x0b-4"tA2$8}H'
            str_1 = 'microsecond'
            dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
            int_0 = -574
            scalar_token_0 = module_0.ScalarToken(dict_0, int_0, int_0)
            any_0 = scalar_token_0.__hash__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
