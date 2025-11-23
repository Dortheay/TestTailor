import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_49(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_38(self):
        str_0 = '255.200.100.75'
        bool_0 = module_0.is_ip(str_0)
        bool_1 = module_0.is_ip(str_0)
        str_1 = '2001:db8:85a3:0000:0000:8a2e:370:?'
        bool_2 = module_0.is_ip(str_1)
        bool_3 = module_0.is_ip(bool_0)
        str_2 = ''
        bool_4 = module_0.is_ip(str_2)

if __name__ == "__main__":
    unittest.main()
