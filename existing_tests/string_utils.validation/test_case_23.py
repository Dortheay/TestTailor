import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        str_0 = "Tqr[$'.'vSD"
        str_1 = '>(<`F0X.3>;$6@ULz4f{'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
        bool_0 = i_s_b_n_checker_0.is_isbn_10()
        bool_1 = module_0.is_ip_v6(str_0)
        str_2 = 'l'
        bool_2 = module_0.is_credit_card(str_2)
        bool_3 = module_0.is_email(str_2)
        i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2)
        bool_4 = i_s_b_n_checker_1.is_isbn_13()
        bool_5 = module_0.contains_html(str_1)

if __name__ == "__main__":
    unittest.main()
