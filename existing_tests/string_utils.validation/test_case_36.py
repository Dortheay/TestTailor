import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        str_0 = '9780470059029'
        str_1 = '9780470059028'
        str_2 = '978047005902X'
        str_3 = '978047005'
        str_4 = '9780470059029123'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_0 = i_s_b_n_checker_0.is_isbn_13()
        i_s_b_n_checker_1 = module_0.__ISBNChecker(str_1)
        bool_1 = i_s_b_n_checker_1.is_isbn_13()
        i_s_b_n_checker_2 = module_0.__ISBNChecker(str_2)
        bool_2 = i_s_b_n_checker_2.is_isbn_13()
        i_s_b_n_checker_3 = module_0.__ISBNChecker(str_3)
        bool_3 = i_s_b_n_checker_3.is_isbn_13()
        i_s_b_n_checker_4 = module_0.__ISBNChecker(str_4)
        bool_4 = i_s_b_n_checker_4.is_isbn_13()

if __name__ == "__main__":
    unittest.main()
