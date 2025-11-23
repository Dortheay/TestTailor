import unittest
import timeout_decorator
import tornado.netutil as module_0
import ssl as module_1

class Test_Netutil_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '127.0.0.1'
        bool_0 = module_0.is_valid_ip(str_0)
        str_1 = '0.0.0.0'
        bool_1 = module_0.is_valid_ip(str_1)
        str_2 = '256.256.256.256'
        bool_2 = module_0.is_valid_ip(str_2)
        str_3 = '192.168.1.1.1'
        bool_3 = module_0.is_valid_ip(str_3)
        str_4 = '192.168.1'
        bool_4 = module_0.is_valid_ip(str_4)
        str_5 = '::1'
        bool_5 = module_0.is_valid_ip(str_5)
        str_6 = '2001:db8::ff00:42:8329'
        bool_6 = module_0.is_valid_ip(str_6)
        str_7 = '2001:db8:::ff00:42:8329'
        bool_7 = module_0.is_valid_ip(str_7)
        var_0 = None
        bool_8 = module_0.is_valid_ip(var_0)
        str_8 = ''
        bool_9 = module_0.is_valid_ip(str_8)
        str_9 = '\x00'
        bool_10 = module_0.is_valid_ip(str_9)
        str_10 = ' '
        bool_11 = module_0.is_valid_ip(str_10)
        bool_12 = module_0.is_valid_ip(str_6)

if __name__ == "__main__":
    unittest.main()
