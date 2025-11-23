import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            int_0 = 1221
            list_0 = module_0.bind_sockets(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
