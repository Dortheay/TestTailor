import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_106(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        float_0 = -1613.0779135693774
        decimal_0 = module_0.Decimal(minimum=float_0, maximum=float_0, exclusive_minimum=float_0, exclusive_maximum=float_0, multiple_of=float_0)

if __name__ == "__main__":
    unittest.main()
