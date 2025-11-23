import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_63(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_62(self):
        try:
            decimal_0 = None
            str_0 = '8N\x0c'
            field_0 = module_0.Field(description=str_0)
            field_1 = module_0.Field()
            union_0 = field_1.__or__(field_0)
            any_0 = union_0.validate(decimal_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
