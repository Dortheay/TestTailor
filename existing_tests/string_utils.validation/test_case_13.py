import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'is_decimal'
        bool_0 = module_0.is_full_string(str_0)
        bool_1 = module_0.is_number(str_0)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_2 = i_s_b_n_checker_0.is_isbn_10()
        bool_3 = module_0.is_email(str_0)
        bool_4 = i_s_b_n_checker_0.is_isbn_10()

if __name__ == "__main__":
    unittest.main()
