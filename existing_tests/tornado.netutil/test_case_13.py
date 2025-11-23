import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = 3406
            str_0 = ''
            int_1 = -1498
            list_0 = module_0.bind_sockets(int_0, str_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
