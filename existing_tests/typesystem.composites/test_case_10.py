import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        field_0 = module_1.Field()
        if_then_else_0 = module_0.IfThenElse(field_0, field_0)
        list_0 = [if_then_else_0]
        bool_0 = False
        field_1 = module_1.Field(default=list_0, allow_null=bool_0)

if __name__ == "__main__":
    unittest.main()
