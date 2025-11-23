import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_127(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_41(self):
        object_0 = module_0.Object()
        bool_0 = True
        str_0 = 'p* B^}|\n5YC\\T!j'
        field_0 = module_0.Field(allow_null=bool_0)
        dict_0 = {str_0: field_0}
        dict_1 = None
        field_1 = None
        object_1 = module_0.Object(pattern_properties=dict_1, additional_properties=field_1)
        any_0 = object_1.validate(dict_0)

if __name__ == "__main__":
    unittest.main()
