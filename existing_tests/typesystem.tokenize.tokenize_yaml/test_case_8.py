import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.fields as module_1

class Test_Tokenize_yaml_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'xo'
            token_0 = module_0.tokenize_yaml(str_0)
            any_0 = module_0.validate_yaml(str_0, token_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
