import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_38(self):
        try:
            number_0 = module_0.Number()
            dict_0 = {}
            str_0 = '6`s'
            bool_0 = None
            field_0 = module_0.Field(description=str_0, allow_null=bool_0)
            str_1 = '\\Fb\x0c#VuxZ>T).'
            field_1 = module_0.Field(description=str_1)
            union_0 = field_1.__or__(field_0)
            time_0 = module_0.Time(**dict_0)
            date_time_0 = module_0.DateTime(**dict_0)
            object_0 = module_0.Object(properties=time_0, max_properties=date_time_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
