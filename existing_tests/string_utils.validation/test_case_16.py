import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '$S`n iU'
        bool_0 = module_0.is_number(str_0)

if __name__ == "__main__":
    unittest.main()
