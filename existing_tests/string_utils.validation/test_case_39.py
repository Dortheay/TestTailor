import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        str_0 = ''
        str_1 = 'k$)4P 3jDlJ8_'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
        bool_0 = i_s_b_n_checker_0.is_isbn_13()
        bool_1 = module_0.is_isbn_13(str_0)
        str_2 = 'oTz=~zj&<\\t6p+H'
        bool_2 = module_0.is_isbn(str_2)
        i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
        bool_3 = i_s_b_n_checker_1.is_isbn_13()
        bool_4 = i_s_b_n_checker_1.is_isbn_10()
        str_3 = "\n    Checks if a given string is a slug (as created by `slugify()`).\n\n    *Examples:*\n\n    >>> is_slug('my-blog-post-title') # returns true\n    >>> is_slug('My blog post title') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :param separator: Join sign used by the slug.\n    :type separator: str\n    :return: True if slug, false otherwise.\n    "
        bool_5 = module_0.is_snake_case(str_3)
        bool_6 = module_0.is_decimal(str_2)
        bool_7 = module_0.is_ip_v4(str_3)
        str_4 = '8'
        bool_8 = module_0.is_integer(str_4)
        bool_9 = module_0.is_email(str_3)
        bool_10 = module_0.is_palindrome(str_4)
        str_5 = '(O8e'
        bool_11 = module_0.is_isbn(str_5)
        str_6 = 'yag*d\rw2;Ae9_{c$P@fA'
        bool_12 = module_0.is_decimal(str_6)
        bool_13 = module_0.is_credit_card(str_5)
        bool_14 = module_0.is_email(bool_1)

if __name__ == "__main__":
    unittest.main()
