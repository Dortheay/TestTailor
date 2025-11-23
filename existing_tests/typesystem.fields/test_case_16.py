import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            float_0 = None
            array_0 = module_0.Array()
            any_0 = array_0.validate(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
