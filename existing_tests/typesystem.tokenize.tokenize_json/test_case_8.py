import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

class Test_Tokenize_json_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '3m\\pH,;T5xDw_M7'
            token_0 = module_0.tokenize_json(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
