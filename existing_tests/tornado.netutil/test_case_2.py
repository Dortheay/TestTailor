import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            blocking_resolver_0 = module_0.BlockingResolver()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
