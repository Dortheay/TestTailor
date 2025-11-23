import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_54(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_53(self):
        try:
            float_0 = -1875.746
            number_0 = module_0.Number(minimum=float_0, multiple_of=float_0)
            any_0 = number_0.validate(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
