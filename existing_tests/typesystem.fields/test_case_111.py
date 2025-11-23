import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_112(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        float_0 = -3003.1567698731096
        number_0 = module_0.Number(minimum=float_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)

if __name__ == "__main__":
    unittest.main()
