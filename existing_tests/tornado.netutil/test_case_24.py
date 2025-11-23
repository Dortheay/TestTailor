import unittest
import timeout_decorator
import tornado.netutil as module_0
import ssl as module_1

class Test_Netutil_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'f!J.L=&w\x0b\tA:<s'
        int_0 = -359
        socket_0 = module_0.bind_unix_socket(str_0, int_0, int_0)
        s_s_l_context_0 = module_1.SSLContext()
        int_1 = 0
        list_0 = module_0.bind_sockets(int_1)

if __name__ == "__main__":
    unittest.main()
