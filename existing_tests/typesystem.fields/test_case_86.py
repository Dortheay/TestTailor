import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_87(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 1426.3552
        field_0 = module_0.Field(default=float_0)

if __name__ == "__main__":
    unittest.main()
