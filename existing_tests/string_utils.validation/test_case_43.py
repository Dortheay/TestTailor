import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_44(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        str_0 = '192.168.1.1'
        str_1 = '0.0.0.0'
        bool_0 = module_0.is_ip_v4(str_1)
        str_2 = '127.0.0.1'
        bool_1 = module_0.is_ip_v4(str_2)
        bool_2 = False
        str_3 = ']v2?KzgSJg%Zb^'
        bool_3 = module_0.is_isbn(str_3)
        str_4 = 'user@domain..com'
        bool_4 = module_0.is_email(str_0)
        str_5 = 'user@domain_domain.com'
        bool_5 = module_0.is_camel_case(bool_1)
        dict_0 = {str_2: bool_4, bool_1: str_5, bool_0: bool_2, bool_4: str_3, bool_3: str_4}
        bool_6 = module_0.is_email(dict_0)
        bool_7 = True
        bool_8 = module_0.is_palindrome(str_5, bool_7)
        str_6 = '7'
        bool_9 = module_0.is_isbn(str_6, bool_5)
        bool_10 = module_0.is_email(bool_4)
        bool_11 = module_0.is_json(bool_10)
        str_7 = 'z\x0c]XBtsni:F02oft$'
        bool_12 = True
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_7, bool_12)
        bool_13 = module_0.is_email(i_s_b_n_checker_0)
        bool_14 = module_0.is_email(str_5)
        bool_15 = module_0.is_ip(str_6)

if __name__ == "__main__":
    unittest.main()
