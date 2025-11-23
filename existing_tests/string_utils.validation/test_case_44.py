import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        str_0 = 'user.name+tag+sorting@example.com'
        bool_0 = module_0.is_email(str_0)
        str_1 = ''
        bool_1 = module_0.is_email(str_1)
        bool_2 = module_0.is_email(bool_1)
        bool_3 = module_0.is_email(str_1)
        str_2 = 'plainaddress'
        bool_4 = module_0.is_email(str_2)
        str_3 = '.startingdot@domain.com'
        bool_5 = module_0.is_email(str_3)
        bool_6 = module_0.is_ip(bool_1)
        bool_7 = module_0.is_ip(bool_6)

if __name__ == "__main__":
    unittest.main()
