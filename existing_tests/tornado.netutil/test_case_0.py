import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'linux'
            int_0 = -1466
            socket_0 = module_0.bind_unix_socket(str_0, int_0)
            str_1 = '48\n>[{9yi2#A~.Rz(\rXB'
            bool_0 = module_0.is_valid_ip(str_1)
            int_1 = 301
            list_0 = module_0.bind_sockets(int_1, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
