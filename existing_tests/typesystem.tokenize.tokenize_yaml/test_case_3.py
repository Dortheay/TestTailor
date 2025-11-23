import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_yaml as module_0

class Test_Tokenize_yaml_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'on'
        token_0 = module_0.tokenize_yaml(str_0)

if __name__ == "__main__":
    unittest.main()
