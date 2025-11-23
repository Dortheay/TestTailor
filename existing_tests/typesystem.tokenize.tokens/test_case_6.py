import unittest
import timeout_decorator
import typesystem.tokenize.tokens as module_0

class Test_Tokens_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            dict_token_0 = module_0.DictToken()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
