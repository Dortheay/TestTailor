import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = '48\n>[{9yi2#A~.Rz(\rXB'
            bool_0 = module_0.is_valid_ip(str_0)
            socket_0 = None
            callable_0 = module_0.add_accept_handler(socket_0, socket_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
