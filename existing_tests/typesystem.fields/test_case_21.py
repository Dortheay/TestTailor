import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            str_0 = '[{|!:'
            str_1 = 'WZ+J'
            bool_0 = True
            field_0 = module_0.Field(description=str_1, default=str_1, allow_null=bool_0)
            validation_error_0 = field_0.validation_error(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
