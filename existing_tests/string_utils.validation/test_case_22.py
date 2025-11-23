import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        float_0 = -587.673
        bool_0 = module_0.is_email(float_0)

if __name__ == "__main__":
    unittest.main()
