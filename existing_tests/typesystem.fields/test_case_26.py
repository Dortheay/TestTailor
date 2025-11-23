import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            bool_0 = False
            decimal_0 = module_1.Decimal()
            integer_0 = module_0.Integer(minimum=decimal_0, maximum=decimal_0, exclusive_maximum=decimal_0)
            str_0 = 'Cannot convert field type '
            string_0 = module_0.String(allow_blank=bool_0, pattern=str_0, format=str_0)
            any_0 = string_0.serialize(str_0)
            float_0 = 1465.79312
            float_1 = -1693.46
            decimal_1 = module_0.Decimal(exclusive_minimum=float_0, multiple_of=float_1)
            object_0 = module_0.Object(property_names=integer_0, min_properties=decimal_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
