import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

class Test_Tokenize_json_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '{"key": "value"}'
            token_0 = module_0.tokenize_json(str_0)
            str_1 = ''
            token_1 = module_0.tokenize_json(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
