import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        float_0 = -445.89533
        bool_0 = module_0.is_isogram(float_0)
        bool_1 = module_0.is_email(float_0)
        str_0 = 'is_number'
        bool_2 = module_0.is_ip_v4(float_0)
        bool_3 = module_0.is_ip_v4(float_0)
        bool_4 = module_0.is_slug(str_0)
        bool_5 = module_0.is_number(str_0)
        bool_6 = module_0.is_slug(bool_1, str_0)
        bool_7 = module_0.is_decimal(str_0)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        str_1 = '\n    Checks if the given string represents a valid ISBN 13 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_13(\'9780312498580\') # returns true\n    >>> is_isbn_13(\'978-0312498580\') # returns true\n    >>> is_isbn_13(\'978-0312498580\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 13, false otherwise.\n    '
        bool_8 = module_0.is_isbn(str_1)
        bool_9 = i_s_b_n_checker_0.is_isbn_10()
        bool_10 = module_0.is_url(str_0)

if __name__ == "__main__":
    unittest.main()
