import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = None
            int_0 = 414
            int_1 = 1824
            socket_0 = module_0.bind_unix_socket(str_0, int_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
