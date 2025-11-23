import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            string_0 = module_0.String()
            choice_0 = module_0.Choice()
            str_0 = None
            array_0 = module_0.Array()
            bool_0 = True
            field_0 = module_0.Field(title=str_0, allow_null=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
