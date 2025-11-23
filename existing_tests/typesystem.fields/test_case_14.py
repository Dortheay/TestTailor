import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            boolean_0 = module_0.Boolean()
            float_0 = None
            any_0 = boolean_0.validate(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
