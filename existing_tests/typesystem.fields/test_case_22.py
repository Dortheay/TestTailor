import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            str_0 = 'additionalProperties'
            tuple_0 = ()
            object_0 = module_0.Object(pattern_properties=tuple_0)
            boolean_0 = module_0.Boolean(description=str_0)
            bool_0 = False
            bool_1 = True
            field_0 = module_0.Field(title=str_0)
            array_0 = module_0.Array(field_0, bool_0)
            any_0 = array_0.serialize(str_0)
            union_0 = field_0.__or__(field_0)
            str_1 = '\rd/m!k&90U;<^J'
            bool_2 = True
            any_1 = module_0.Any(title=str_1, allow_null=bool_2)
            any_2 = any_1.validate(boolean_0)
            any_3 = boolean_0.validate(bool_1)
            any_4 = boolean_0.validate(boolean_0, strict=bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
