import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        try:
            int_0 = 1920
            str_0 = module_0.roman_encode(int_0)
            str_1 = "1|'T%(}!K4"
            str_2 = '{!MKiR?n2A9x|^'
            str_3 = module_0.snake_case_to_camel(str_1, str_0)
            str_4 = "\n    Checks if the string is a pangram (https://en.wikipedia.org/wiki/Pangram).\n\n    *Examples:*\n\n    >>> is_pangram('The quick brown fox jumps over the lazy dog') # returns true\n    >>> is_pangram('hello world') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if the string is a pangram, False otherwise.\n    "
            dict_0 = {str_2: str_2, str_4: str_2, str_1: str_2}
            string_compressor_0 = module_0.__StringCompressor(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
