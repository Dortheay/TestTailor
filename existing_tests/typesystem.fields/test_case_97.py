import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_98(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        str_0 = '\ng&c}4H`C'
        field_0 = module_0.Field()
        array_0 = module_0.Array(field_0, field_0)
        any_0 = array_0.serialize(str_0)
        field_1 = module_0.Field(title=str_0, default=str_0)
        decimal_0 = module_1.Decimal()
        union_0 = field_0.__or__(field_1)
        array_1 = module_0.Array(field_1)

if __name__ == "__main__":
    unittest.main()
