import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_53(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_42(self):
        str_0 = '255.200.100.75'
        bool_0 = module_0.is_ip(str_0)
        str_1 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
        bool_1 = module_0.is_ip(str_1)
        str_2 = '1.2.3'
        bool_2 = module_0.is_ip(str_2)
        str_3 = '2001:db8:85a3:0000:0000:8a2e:370:?'
        bool_3 = module_0.is_ip(str_3)
        str_4 = 'not_an_ip'
        bool_4 = module_0.is_ip(str_4)
        str_5 = ''
        bool_5 = module_0.is_ip(str_5)
        int_0 = 12345
        bool_6 = module_0.is_ip(int_0)

if __name__ == "__main__":
    unittest.main()
