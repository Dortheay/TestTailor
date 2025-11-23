import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'F(\xe2\xfb\xe6P\xf4\x06qy'
            bool_0 = module_0.is_camel_case(bytes_0)
            bool_1 = module_0.is_credit_card(bytes_0)
            bool_2 = module_0.is_url(bytes_0)
            bool_3 = module_0.is_ip_v6(bytes_0)
            str_0 = 'is_json'
            i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
            bool_4 = i_s_b_n_checker_0.is_isbn_13()
            str_1 = None
            bool_5 = module_0.is_isbn(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
