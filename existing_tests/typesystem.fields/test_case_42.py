import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_42(self):
        try:
            bool_0 = False
            field_0 = module_0.Field(allow_null=bool_0)
            field_1 = module_0.Field()
            optional_0 = None
            str_0 = ':R3tvufK5Q\\rt'
            decimal_0 = module_0.Decimal(precision=str_0)
            any_0 = decimal_0.serialize(optional_0)
            any_1 = decimal_0.serialize(optional_0)
            any_2 = decimal_0.serialize(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
