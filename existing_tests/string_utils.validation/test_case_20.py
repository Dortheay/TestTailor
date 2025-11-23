import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = 'E3>\x0c)q[G@\r@v#'
        bool_0 = module_0.is_full_string(str_0)
        list_0 = [bool_0, str_0]
        bool_1 = module_0.is_url(str_0, list_0)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_0)
        bool_2 = i_s_b_n_checker_0.is_isbn_13()
        str_1 = ';gfji0$BA(el;L^uU:'
        bool_3 = module_0.is_integer(str_1)
        bool_4 = module_0.is_isogram(bool_3)
        bool_5 = module_0.is_number(str_0)
        int_0 = module_0.words_count(str_1)
        i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
        bool_6 = i_s_b_n_checker_1.is_isbn_10()
        bool_7 = True
        i_s_b_n_checker_2 = module_0.__ISBNChecker(str_1, bool_7)
        bool_8 = module_0.is_number(str_0)
        bool_9 = i_s_b_n_checker_1.is_isbn_10()
        bool_10 = i_s_b_n_checker_1.is_isbn_13()
        bool_11 = i_s_b_n_checker_2.is_isbn_13()

if __name__ == "__main__":
    unittest.main()
