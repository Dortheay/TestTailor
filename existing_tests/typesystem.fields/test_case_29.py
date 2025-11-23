import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            bool_0 = True
            str_0 = '|3Q|`jF!\nG'
            str_1 = "F8W?%O+@OhVLya?A'R"
            field_0 = module_0.Field(title=str_0, description=str_1, allow_null=bool_0)
            any_0 = field_0.get_default_value()
            str_2 = None
            bool_1 = False
            field_1 = module_0.Field(title=str_1, description=str_2, allow_null=bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
