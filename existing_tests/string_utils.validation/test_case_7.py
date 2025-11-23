import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'EK-'
            str_1 = 'y'
            i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
            bool_0 = True
            bool_1 = module_0.is_palindrome(str_1, bool_0, bool_0)
            bool_2 = module_0.is_integer(str_0)
            bool_3 = module_0.is_ip(str_0)
            bool_4 = module_0.is_camel_case(str_1)
            str_2 = 'RIHOT_SPACE'
            i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2)
            int_0 = -3822
            bool_5 = module_0.is_snake_case(int_0)
            bool_6 = i_s_b_n_checker_0.is_isbn_13()
            bool_7 = i_s_b_n_checker_0.is_isbn_10()
            bool_8 = module_0.is_email(str_1)
            bool_9 = module_0.is_ip(i_s_b_n_checker_0)
            str_3 = '{'
            bool_10 = module_0.is_string(bool_2)
            bool_11 = module_0.is_isbn_13(str_3)
            bool_12 = module_0.is_ip(i_s_b_n_checker_1)
            bool_13 = module_0.is_json(str_1)
            bool_14 = module_0.is_url(str_0)
            bool_15 = i_s_b_n_checker_0.is_isbn_13()
            str_4 = ';$,'
            bool_16 = module_0.is_isbn(str_2, bool_8)
            bool_17 = i_s_b_n_checker_1.is_isbn_13()
            bool_18 = module_0.is_credit_card(str_3)
            bool_19 = i_s_b_n_checker_0.is_isbn_10()
            str_5 = "\n    Checks if an object is a string.\n\n    *Example:*\n\n    >>> is_string('foo') # returns true\n    >>> is_string(b'foo') # returns false\n\n    :param obj: Object to test.\n    :return: True if string, false otherwise.\n    "
            bool_20 = module_0.is_decimal(str_5)
            bool_21 = module_0.is_credit_card(str_4, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
