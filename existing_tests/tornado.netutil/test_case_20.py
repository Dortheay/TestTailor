import unittest
import timeout_decorator
import tornado.netutil as module_0
import ssl as module_1

class Test_Netutil_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'D\r&%(\n\rEk[4+k'
        socket_0 = module_0.bind_unix_socket(str_0)
        str_1 = ''
        bool_0 = module_0.is_valid_ip(str_1)

if __name__ == "__main__":
    unittest.main()
