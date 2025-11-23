import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        str_0 = 'k%C]"v'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_0 = i_s_b_n_checker_0.is_isbn_10()
        bool_1 = module_0.is_ip_v4(i_s_b_n_checker_0)

if __name__ == "__main__":
    unittest.main()
