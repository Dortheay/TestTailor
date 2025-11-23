import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        str_0 = 'uy'
        str_1 = 'k$)4P 3jDlJ8_'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
        bool_0 = i_s_b_n_checker_0.is_isbn_13()
        bool_1 = module_0.is_isbn_13(str_0)
        str_2 = 'oTz=~zj&<\\t6p+H'
        bool_2 = module_0.is_isbn(str_2)
        str_3 = 'nci{`yjY"y\t<?g}Vg'
        i_s_b_n_checker_1 = module_0.__ISBNChecker(str_3)
        bool_3 = i_s_b_n_checker_1.is_isbn_13()
        bool_4 = i_s_b_n_checker_1.is_isbn_10()
        bool_5 = module_0.is_decimal(str_2)
        bool_6 = module_0.is_ip_v4(bool_0)
        str_4 = '8'
        bool_7 = module_0.is_ip_v6(bool_4)
        bool_8 = module_0.is_email(i_s_b_n_checker_1)
        str_5 = 'H_IjDw.bDs'
        bool_9 = module_0.is_url(i_s_b_n_checker_0, i_s_b_n_checker_1)
        bool_10 = module_0.is_isbn_10(str_4)
        bool_11 = module_0.is_decimal(str_0)
        bool_12 = module_0.is_ip(str_5)
        bool_13 = module_0.is_json(str_4)
        bool_14 = module_0.is_decimal(str_4)
        bool_15 = i_s_b_n_checker_1.is_isbn_10()
        bool_16 = i_s_b_n_checker_0.is_isbn_13()
        bool_17 = i_s_b_n_checker_1.is_isbn_10()
        str_6 = '_-NA*M/\x0bHO?1qnZc/H$d'
        bool_18 = module_0.is_decimal(str_1)
        bool_19 = module_0.is_credit_card(str_4)
        bool_20 = module_0.is_email(str_6)

if __name__ == "__main__":
    unittest.main()
