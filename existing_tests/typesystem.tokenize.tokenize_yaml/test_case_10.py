import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.fields as module_1

class Test_Tokenize_yaml_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'zuk{dmhH@2V8zI0[::'
            bool_0 = True
            field_0 = module_1.Field(allow_null=bool_0)
            any_0 = module_0.validate_yaml(str_0, field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
