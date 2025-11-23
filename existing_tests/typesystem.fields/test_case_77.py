import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_78(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_77(self):
        try:
            int_0 = 965
            number_0 = module_0.Number(minimum=int_0, exclusive_maximum=int_0)
            float_0 = -598.1639
            bool_0 = True
            any_0 = number_0.validate(float_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
