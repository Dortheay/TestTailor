import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_72(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_71(self):
        try:
            array_0 = module_0.Array()
            choice_0 = module_0.Choice()
            str_0 = 'A'
            field_0 = module_0.Field(description=str_0)
            str_1 = None
            dict_0 = {str_0: field_0, str_1: field_0, str_1: field_0}
            date_0 = module_0.Date()
            object_0 = module_0.Object(properties=choice_0, pattern_properties=dict_0, property_names=field_0, max_properties=date_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
