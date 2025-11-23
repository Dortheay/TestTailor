import unittest
import timeout_decorator
import ansible.parsing.utils.addresses as module_0

class Test_Addresses_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '192.168.1.1'
            var_0 = module_0.parse_address(str_0)
            str_1 = '192.168.1.1:8080'
            var_1 = module_0.parse_address(str_1)
            str_2 = '[2001:db8::1]:443'
            var_2 = module_0.parse_address(str_2)
            str_3 = 'example.com'
            var_3 = module_0.parse_address(str_3)
            str_4 = 'example.com:80'
            var_4 = module_0.parse_address(str_4)
            str_5 = 'invalid_host!'
            var_5 = module_0.parse_address(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
