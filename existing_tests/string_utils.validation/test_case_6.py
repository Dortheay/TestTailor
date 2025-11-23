import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bool_0 = None
            bool_1 = module_0.is_credit_card(bool_0)
            int_0 = 320
            bool_2 = module_0.is_full_string(bool_1)
            bool_3 = module_0.is_slug(int_0)
            str_0 = ' Uy; Ull]i\\'
            bool_4 = True
            bool_5 = module_0.is_url(bool_4)
            str_1 = 'OkuM\x0c!=\nGK=14uEP'
            str_2 = '[10@\r4t\x0c@:5'
            bool_6 = module_0.is_decimal(str_2)
            i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
            bool_7 = i_s_b_n_checker_0.is_isbn_10()
            bool_8 = module_0.is_uuid(bool_1, bool_4)
            bool_9 = i_s_b_n_checker_0.is_isbn_10()
            bool_10 = i_s_b_n_checker_0.is_isbn_10()
            float_0 = 423.679
            bool_11 = module_0.is_ip_v4(str_0)
            i_s_b_n_checker_1 = module_0.__ISBNChecker(str_0)
            bool_12 = i_s_b_n_checker_1.is_isbn_13()
            bool_13 = i_s_b_n_checker_1.is_isbn_10()
            bool_14 = module_0.contains_html(str_0)
            bool_15 = module_0.is_isogram(float_0)
            bool_16 = module_0.is_json(bool_0)
            bool_17 = module_0.is_full_string(int_0)
            bool_18 = module_0.is_pangram(bool_3)
            str_3 = None
            bool_19 = True
            bool_20 = module_0.is_isbn_10(str_3, bool_19)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
