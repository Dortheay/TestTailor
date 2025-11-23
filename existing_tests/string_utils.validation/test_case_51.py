import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_52(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_41(self):
        str_0 = '255.200.100.75'
        bool_0 = module_0.is_ip(str_0)
        str_1 = '0.0.0.0'
        bool_1 = module_0.is_ip_v4(str_1)
        str_2 = '127.0.0.1'
        bool_2 = module_0.is_ip_v4(str_2)
        str_3 = ']v2?KzgSJg%Zb^'
        bool_3 = module_0.is_isbn(str_3)
        bool_4 = module_0.is_email(str_3)
        bool_5 = module_0.is_camel_case(bool_2)
        str_4 = 'foo@bar.com'
        str_5 = '"user@domain".replace("\\ ", "")'
        bool_6 = module_0.is_email(str_5)
        bool_7 = module_0.is_email(bool_5)
        bool_8 = module_0.is_email(str_4)
        str_6 = 'valid."user"@domain.com'
        bool_9 = module_0.is_email(str_6)

if __name__ == "__main__":
    unittest.main()
