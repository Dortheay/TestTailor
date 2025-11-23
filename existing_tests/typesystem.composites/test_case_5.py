import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            tuple_0 = ()
            bool_0 = False
            str_0 = ':ZHi tKe_D+wSo>!>6'
            field_0 = module_1.Field(description=str_0, default=str_0)
            if_then_else_0 = module_0.IfThenElse(field_0, field_0, field_0)
            any_0 = if_then_else_0.validate(tuple_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
