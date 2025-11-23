import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            str_0 = 'x!)9Q:'
            field_0 = module_0.Field()
            dict_0 = {str_0: field_0}
            dict_1 = {str_0: field_0}
            object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0, additional_properties=field_0, required=dict_1)
            int_0 = 1
            decimal_0 = module_0.Decimal(minimum=int_0, exclusive_maximum=int_0, multiple_of=int_0)
            any_0 = decimal_0.serialize(object_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
