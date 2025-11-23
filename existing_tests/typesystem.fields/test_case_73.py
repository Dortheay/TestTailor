import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_74(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_73(self):
        try:
            object_0 = module_0.Object()
            bool_0 = False
            str_0 = 'Wq_'
            field_0 = module_0.Field(title=str_0)
            int_0 = 3702
            bool_1 = True
            array_0 = module_0.Array(field_0, field_0, int_0, int_0, int_0, bool_1)
            any_0 = array_0.validate(int_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
