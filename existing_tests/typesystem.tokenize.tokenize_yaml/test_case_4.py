import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_yaml as module_0

class Test_Tokenize_yaml_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '\n    name: John Doe\n    age: 30\n    '
        token_0 = module_0.tokenize_yaml(str_0)

if __name__ == "__main__":
    unittest.main()
