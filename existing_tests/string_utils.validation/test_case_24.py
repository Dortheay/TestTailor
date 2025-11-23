import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        str_0 = 'V/d/AIEmo8/\x0bA'
        bool_0 = module_0.is_ip_v4(str_0)
        str_1 = '\n    Checks if the given string contains HTML/XML tags.\n\n    By design, this function matches ANY type of tag, so don\'t expect to use it\n    as an HTML validator, its goal is to detect "malicious" or undesired tags in the text.\n\n    *Examples:*\n\n    >>> contains_html(\'my string is <strong>bold</strong>\') # returns true\n    >>> contains_html(\'my string is not bold\') # returns false\n\n    :param input_string: Text to check\n    :type input_string: str\n    :return: True if string contains html, false otherwise.\n    '
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1, bool_0)
        bool_1 = module_0.is_integer(str_1)
        bool_2 = module_0.is_credit_card(i_s_b_n_checker_0)
        bool_3 = module_0.is_snake_case(str_0, str_1)
        bool_4 = i_s_b_n_checker_0.is_isbn_10()

if __name__ == "__main__":
    unittest.main()
