import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_60(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_59(self):
        try:
            str_0 = '\ng&c}4H`C'
            field_0 = module_0.Field()
            str_1 = 'e 6'
            bool_0 = False
            field_1 = module_0.Field(title=str_1, allow_null=bool_0)
            any_0 = field_1.get_default_value()
            array_0 = module_0.Array(field_0, field_0)
            any_1 = array_0.serialize(str_0)
            string_0 = module_0.String()
            date_0 = None
            decimal_0 = module_0.Decimal(maximum=string_0, exclusive_maximum=date_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
