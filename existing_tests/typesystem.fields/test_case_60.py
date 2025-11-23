import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_61(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_60(self):
        try:
            float_0 = -1613.0779135693774
            int_0 = 2
            number_0 = module_0.Number(maximum=float_0, exclusive_minimum=float_0)
            any_0 = number_0.validate(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
