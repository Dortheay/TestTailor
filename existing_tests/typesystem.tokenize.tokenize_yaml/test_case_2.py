import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_yaml as module_0

class Test_Tokenize_yaml_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'6\xf8'
        token_0 = module_0.tokenize_yaml(bytes_0)

if __name__ == "__main__":
    unittest.main()
