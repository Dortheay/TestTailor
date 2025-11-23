import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        str_0 = '\\'
        bool_0 = module_0.is_ip(str_0)
        bool_1 = module_0.is_slug(bool_0)
        bool_2 = module_0.is_isogram(bool_1)
        str_1 = 'O'
        bool_3 = module_0.is_decimal(str_1)
        bool_4 = module_0.is_ip(bool_3)
        bool_5 = module_0.is_slug(bool_0)

if __name__ == "__main__":
    unittest.main()
