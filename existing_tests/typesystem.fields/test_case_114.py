import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_115(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        float_0 = 621.39
        float_1 = -3040.216
        number_0 = module_0.Number(maximum=float_0, exclusive_maximum=float_0)
        time_0 = module_0.Time()
        any_0 = number_0.validate(float_1)

if __name__ == "__main__":
    unittest.main()
