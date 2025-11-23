import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        str_0 = ']906B'
        bool_0 = module_0.is_camel_case(str_0)
        bool_1 = module_0.is_isogram(str_0)
        bool_2 = module_0.is_email(str_0)
        dict_0 = None
        bool_3 = module_0.is_slug(dict_0)
        str_1 = 'T4?Ug8\x0cE4/gEE'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
        bool_4 = i_s_b_n_checker_0.is_isbn_13()

if __name__ == "__main__":
    unittest.main()
