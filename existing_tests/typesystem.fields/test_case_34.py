import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        try:
            int_0 = -1209
            decimal_0 = module_1.Decimal()
            field_0 = module_0.Field(default=decimal_0)
            bool_0 = True
            field_1 = module_0.Field(allow_null=bool_0)
            union_0 = field_1.__or__(field_0)
            number_0 = module_0.Number(minimum=decimal_0, maximum=int_0)
            any_0 = number_0.validate(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
