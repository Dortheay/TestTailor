import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            socket_0 = module_1.socket()
            list_0 = []
            dict_0 = {}
            s_s_l_context_0 = module_2.SSLContext(*list_0, **dict_0)
            s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
            str_0 = '3'
            bool_0 = module_0.is_valid_ip(str_0)
            int_0 = 1469
            int_1 = 347
            list_1 = module_0.bind_sockets(int_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
