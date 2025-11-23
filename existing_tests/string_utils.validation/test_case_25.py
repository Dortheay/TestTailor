import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        str_0 = 'u2BuTP!"J@Wfe|"Ca;o'
        bool_0 = module_0.is_camel_case(str_0)

if __name__ == "__main__":
    unittest.main()
