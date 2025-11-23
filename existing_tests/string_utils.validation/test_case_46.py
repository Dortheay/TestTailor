import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_47(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_36(self):
        str_0 = '255.200.100.75'
        bool_0 = module_0.is_ip(str_0)
        str_1 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
        bool_1 = module_0.is_ip(str_1)
        str_2 = '1.2.3'
        bool_2 = module_0.is_ip(str_2)
        str_3 = '2001:db8:85a3:0000:0000:8a2e:370:?'
        bool_3 = module_0.is_ip(str_3)
        bool_4 = module_0.is_email(bool_3)
        bytes_0 = b'\x8d\xd3\xb1z6\x8b\xbd\xe3eV\x1e\xda\xbd-mT\xc7\xa31'
        bool_5 = module_0.is_email(bytes_0)
        str_4 = 'email.@domain.com'
        str_5 = 'abfDi\rBTo0LX=0QI'
        bool_6 = module_0.is_email(str_5)
        bool_7 = module_0.is_email(bool_3)
        bool_8 = module_0.is_email(str_4)
        bool_9 = module_0.is_email(bool_1)
        str_6 = 'email@domain..com'
        bool_10 = module_0.is_email(str_6)

if __name__ == "__main__":
    unittest.main()
