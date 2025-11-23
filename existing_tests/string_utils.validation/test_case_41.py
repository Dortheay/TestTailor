import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        str_0 = "((?<=\\w)\\'\\ss\\s|(?<=\\w)\\s\\'s(?=\\w)|(?<=\\w)\\s\\'s\\s(?=\\w))"
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_0 = i_s_b_n_checker_0.is_isbn_10()
        str_1 = ' $Ih&4FDdIJN|U8g'
        bool_1 = module_0.is_ip(str_1)
        str_2 = 'Y=_iVE$XJ'
        bool_2 = module_0.is_email(str_2)
        i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2)
        str_3 = '_{/5^^C$=JF"\nLu'
        bool_3 = module_0.is_decimal(str_3)
        str_4 = 'is_palindrome'
        bool_4 = module_0.is_isbn(str_4)
        bool_5 = i_s_b_n_checker_0.is_isbn_10()
        str_5 = '{'
        bool_6 = module_0.is_isbn_13(str_5)
        str_6 = ' ]/K`ZvrT;`Kc3'
        bool_7 = module_0.is_url(i_s_b_n_checker_1, str_6)
        str_7 = '/'
        bool_8 = module_0.is_palindrome(str_7, bool_1)

if __name__ == "__main__":
    unittest.main()
