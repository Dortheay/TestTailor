import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        str_0 = 'd'
        int_0 = module_0.words_count(str_0)
        str_1 = 'RI[||6|<iEk'
        bool_0 = module_0.is_isogram(str_1)
        str_2 = '6N(=*'
        bool_1 = False
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2, bool_1)
        bool_2 = i_s_b_n_checker_0.is_isbn_13()
        bool_3 = True
        str_3 = '73\nh /4'
        int_1 = module_0.words_count(str_3)
        i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1, bool_3)
        bool_4 = i_s_b_n_checker_1.is_isbn_13()
        bool_5 = module_0.is_palindrome(str_1)
        bool_6 = module_0.is_url(str_1)

if __name__ == "__main__":
    unittest.main()
