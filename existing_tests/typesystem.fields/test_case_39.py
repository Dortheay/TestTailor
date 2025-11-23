import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_39(self):
        try:
            float_0 = -1613.0779135693774
            str_0 = 'm.[0W7A]yxz=ACI:|KL'
            number_0 = module_0.Number(minimum=float_0, maximum=float_0, precision=str_0)
            any_0 = number_0.validate(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
