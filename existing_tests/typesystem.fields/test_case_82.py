import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_83(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_82(self):
        try:
            object_0 = module_0.Object()
            bool_0 = False
            int_0 = 5
            str_0 = 'p* B^}|\n5YC\\T!j'
            field_0 = module_0.Field(allow_null=bool_0)
            dict_0 = {str_0: field_0}
            any_0 = module_0.Any(default=field_0)
            object_1 = module_0.Object(properties=dict_0, max_properties=int_0)
            any_1 = object_1.validate(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
