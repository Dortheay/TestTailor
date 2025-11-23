import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_48(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_47(self):
        try:
            str_0 = 'RIs{-:zPID%KJ'
            field_0 = module_0.Field(title=str_0, description=str_0)
            dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
            object_0 = module_0.Object(properties=dict_0, additional_properties=field_0, property_names=field_0)
            any_0 = object_0.validate(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
