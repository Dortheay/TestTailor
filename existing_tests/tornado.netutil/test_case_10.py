import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'f!J.L=&w\x0b\tA:<s'
            int_0 = -373
            int_1 = -1013
            socket_0 = module_0.bind_unix_socket(str_0, int_0, int_1)
            str_1 = '48\n>[{9yi2#A~.Rz(\rXB'
            dict_0 = {str_1: int_0}
            s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
