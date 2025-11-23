import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.fields as module_1

class Test_Tokenize_yaml_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '- item1\n- item2'
            token_0 = module_0.tokenize_yaml(str_0)
            token_1 = module_0.tokenize_yaml(str_0)
            token_2 = module_0.tokenize_yaml(str_0)
            str_1 = ''
            token_3 = module_0.tokenize_yaml(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
