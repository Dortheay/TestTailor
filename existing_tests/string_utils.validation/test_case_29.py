import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        str_0 = '\n    Checks if a string is a valid ip v6.\n\n    *Examples:*\n\n    >>> is_ip_v6(\'2001:db8:85a3:0000:0000:8a2e:370:7334\') # returns true\n    >>> is_ip_v6(\'2001:db8:85a3:0000:0000:8a2e:370:?\') # returns false (invalid "?")\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if a v6 ip, false otherwise.\n    '
        int_0 = module_0.words_count(str_0)
        bool_0 = module_0.is_ip(int_0)
        bool_1 = module_0.is_camel_case(bool_0)

if __name__ == "__main__":
    unittest.main()
