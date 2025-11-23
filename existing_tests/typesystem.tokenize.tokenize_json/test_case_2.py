import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

class Test_Tokenize_json_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '['
            token_0 = module_0.tokenize_json(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
