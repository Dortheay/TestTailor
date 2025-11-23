import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'valid_string'
            str_1 = 'valid_string'
            list_0 = []
            dict_0 = {}
            all_of_0 = module_0.AllOf(list_0, **dict_0)
            any_0 = all_of_0.validate(str_0)
            one_of_0 = module_0.OneOf(list_0)
            field_0 = module_1.Field()
            str_2 = 'zNT;Q]iQR\\8gh>1wcu'
            dict_1 = {str_1: list_0, str_2: one_of_0, str_0: str_2, str_2: list_0}
            if_then_else_0 = module_0.IfThenElse(field_0, field_0, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
