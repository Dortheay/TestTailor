import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        try:
            int_0 = 1922
            str_0 = 'gI'
            str_1 = module_0.shuffle(str_0)
            str_2 = module_0.roman_encode(int_0)
            str_3 = "\n    Check if a string is a valid email.\n\n    Reference: https://tools.ietf.org/html/rfc3696#section-3\n\n    *Examples:*\n\n    >>> is_email('my.email@the-provider.com') # returns true\n    >>> is_email('@gmail.com') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if email, false otherwise.\n    "
            str_4 = module_0.prettify(str_3)
            str_5 = "1|'T%(}!K4"
            str_6 = module_0.snake_case_to_camel(str_4)
            str_7 = module_0.strip_margin(str_1)
            list_0 = [str_0, str_5]
            var_0 = module_0.camel_case_to_snake(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
