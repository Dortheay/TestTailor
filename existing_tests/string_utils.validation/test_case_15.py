import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        bool_0 = None
        bool_1 = module_0.is_isogram(bool_0)

if __name__ == "__main__":
    unittest.main()
