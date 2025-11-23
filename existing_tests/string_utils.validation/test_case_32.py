import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        str_0 = 'D\t(If4+D'
        bool_0 = module_0.is_pangram(str_0)
        str_1 = '$S`n iU'
        bool_1 = module_0.is_number(str_1)

if __name__ == "__main__":
    unittest.main()
