import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_51(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_40(self):
        str_0 = '255.200.100.75'
        bool_0 = module_0.is_ip(str_0)
        str_1 = '192.168.1.1'
        bool_1 = module_0.is_email(str_0)
        bool_2 = module_0.is_email(bool_0)
        str_2 = ' '
        bool_3 = module_0.is_email(str_0)
        bool_4 = module_0.is_email(str_0)
        str_3 = 'plain.address@domain'
        bool_5 = module_0.is_email(str_1)
        bool_6 = module_0.is_email(str_1)
        bool_7 = module_0.is_email(bool_1)
        str_4 = 'email@[123.123.123.123]'
        bool_8 = module_0.is_email(str_3)
        bool_9 = module_0.is_email(str_4)
        bool_10 = module_0.is_uuid(bool_1, bool_3)
        bool_11 = module_0.is_email(str_2)
        str_5 = 'email..email@domain.com'
        bool_12 = module_0.is_email(str_2)
        bool_13 = module_0.is_json(bool_6)
        bool_14 = module_0.is_email(str_5)
        bool_15 = module_0.is_email(str_2)

if __name__ == "__main__":
    unittest.main()
