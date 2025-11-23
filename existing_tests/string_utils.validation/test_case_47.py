import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_48(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_37(self):
        str_0 = '9780312498580'
        bool_0 = module_0.is_email(str_0)
        str_1 = 'user@domain'
        bool_1 = module_0.is_email(bool_0)
        str_2 = 'user.name+tag+sorting@example.com'
        bool_2 = module_0.is_email(str_1)
        bool_3 = module_0.is_email(str_2)
        bool_4 = module_0.is_email(bool_0)
        bool_5 = module_0.is_email(str_2)
        bool_6 = module_0.is_email(str_0)
        bool_7 = module_0.is_email(bool_0)
        bool_8 = module_0.is_email(str_1)
        str_3 = '"email"@[123.123.123.123]'
        bool_9 = module_0.is_email(str_3)
        bool_10 = module_0.is_email(bool_1)
        bool_11 = module_0.is_email(str_0)
        bool_12 = module_0.is_email(str_3)
        bool_13 = module_0.is_email(bool_11)
        bool_14 = module_0.is_email(bool_3)
        bool_15 = module_0.is_email(bool_4)

if __name__ == "__main__":
    unittest.main()
