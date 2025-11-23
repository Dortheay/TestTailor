import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = 1082
            decimal_0 = module_1.Decimal()
            number_0 = module_0.Number(maximum=int_0, exclusive_maximum=int_0, multiple_of=int_0)
            boolean_0 = module_0.Boolean()
            any_0 = boolean_0.validate(decimal_0)
            any_1 = number_0.validate(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
