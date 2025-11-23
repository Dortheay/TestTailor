import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_124(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_38(self):
        str_0 = '(h'
        field_0 = module_0.Field()
        dict_0 = {str_0: field_0}
        int_0 = 0
        dict_1 = {}
        object_0 = module_0.Object(pattern_properties=dict_0, min_properties=int_0, max_properties=int_0, **dict_1)
        any_0 = object_0.validate(dict_1)

if __name__ == "__main__":
    unittest.main()
