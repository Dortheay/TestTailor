import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_102(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        float_0 = -1613.0779135693774
        const_0 = module_0.Const(float_0)
        number_0 = module_0.Number(maximum=float_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)

if __name__ == "__main__":
    unittest.main()
