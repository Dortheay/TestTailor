import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            any_0 = module_0.Any(allow_null=bool_0)
            float_0 = None
            string_0 = module_0.String()
            any_1 = string_0.validate(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
