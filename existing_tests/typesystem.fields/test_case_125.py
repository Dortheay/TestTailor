import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_126(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_40(self):
        str_0 = '(h'
        field_0 = module_0.Field()
        dict_0 = {str_0: field_0}
        int_0 = 0
        dict_1 = {}
        object_0 = module_0.Object(properties=dict_0, min_properties=int_0)
        bool_0 = True
        any_0 = object_0.validate(dict_1, strict=bool_0)
        any_1 = object_0.validate(dict_1)

if __name__ == "__main__":
    unittest.main()
