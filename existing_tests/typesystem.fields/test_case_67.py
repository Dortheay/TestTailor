import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_68(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_67(self):
        try:
            str_0 = None
            field_0 = None
            str_1 = None
            dict_0 = {str_0: field_0, str_0: field_0, str_1: field_0}
            bool_0 = True
            field_1 = module_0.Field(allow_null=bool_0)
            object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0, additional_properties=field_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
