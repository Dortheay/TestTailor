import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'f!J.L=&w\x0b\tA:<s'
            int_0 = -359
            socket_0 = module_0.bind_unix_socket(str_0, int_0, int_0)
            s_s_l_context_0 = module_2.SSLContext()
            s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
            address_family_0 = module_1.AddressFamily.AF_UNIX
            list_0 = module_0.bind_sockets(int_0, address_family_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
