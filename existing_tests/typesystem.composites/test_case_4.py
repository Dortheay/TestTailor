import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            union_0 = None
            str_0 = 'Dsp7":LGX'
            field_0 = module_1.Field(title=str_0)
            if_then_else_0 = module_0.IfThenElse(field_0)
            any_0 = if_then_else_0.validate(union_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
