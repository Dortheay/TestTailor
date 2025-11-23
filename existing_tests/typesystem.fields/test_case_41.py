import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_41(self):
        try:
            str_0 = '\ng&c}4H`C'
            bool_0 = True
            field_0 = module_0.Field(description=str_0, allow_null=bool_0)
            any_0 = field_0.get_default_value()
            field_1 = module_0.Field(title=str_0, default=str_0)
            int_0 = 1148
            array_0 = module_0.Array(field_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
