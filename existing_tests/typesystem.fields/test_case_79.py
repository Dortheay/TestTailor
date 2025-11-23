import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_80(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_79(self):
        try:
            float_0 = None
            array_0 = module_0.Array()
            bool_0 = False
            bool_1 = False
            field_0 = module_0.Field(allow_null=bool_1)
            bool_2 = True
            field_1 = module_0.Field(allow_null=bool_2)
            union_0 = field_1.__or__(field_0)
            any_0 = union_0.validate(float_0, bool_0)
            int_0 = 770
            number_0 = module_0.Number(exclusive_maximum=int_0, multiple_of=int_0)
            any_1 = number_0.validate(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
