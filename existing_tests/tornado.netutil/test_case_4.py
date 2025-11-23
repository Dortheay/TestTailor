import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            list_0 = []
            threaded_resolver_0 = module_0.ThreadedResolver(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
