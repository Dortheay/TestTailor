import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        bool_0 = True
        bool_1 = module_0.is_palindrome(bool_0)
        str_0 = '\n    Restore a previously compressed string (obtained using `compress()`) back to its original state.\n\n    :param input_string: String to restore.\n    :type input_string: str\n    :param encoding: Original string encoding.\n    :type encoding: str\n    :return: Decompressed string.\n    '
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)

if __name__ == "__main__":
    unittest.main()
