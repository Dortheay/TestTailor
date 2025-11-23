import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        str_0 = ']906B'
        bool_0 = module_0.is_camel_case(str_0)
        bool_1 = module_0.is_email(str_0)

if __name__ == "__main__":
    unittest.main()
