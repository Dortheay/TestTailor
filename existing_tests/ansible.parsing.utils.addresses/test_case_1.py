import unittest
import timeout_decorator
import ansible.parsing.utils.addresses as module_0

class Test_Addresses_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '192.168.1.1:80'
            var_0 = module_0.parse_address(str_0)
            str_1 = '[2001:0db8::1]:443'
            var_1 = module_0.parse_address(str_1)
            str_2 = 'example.com'
            var_2 = module_0.parse_address(str_2)
            str_3 = 'example.com:8080'
            var_3 = module_0.parse_address(str_3)
            str_4 = '127.0.0.1'
            var_4 = module_0.parse_address(str_4)
            str_5 = 'example[1:3].com'
            bool_0 = True
            var_5 = module_0.parse_address(str_5, bool_0)
            str_6 = 'example[1:3].com'
            bool_1 = False
            var_6 = module_0.parse_address(str_6, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
