import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_110(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        str_0 = '\ng&c}4H`C'
        field_0 = module_0.Field(title=str_0, default=str_0)
        int_0 = 1148
        array_0 = module_0.Array(field_0, field_0, int_0, int_0)

if __name__ == "__main__":
    unittest.main()
