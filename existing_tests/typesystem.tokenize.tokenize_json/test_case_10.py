import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

class Test_Tokenize_json_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'false'
            field_0 = module_1.Field(description=str_0, default=str_0)
            any_0 = module_0.validate_json(str_0, field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
