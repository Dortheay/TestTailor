import unittest
import timeout_decorator
import tornado.netutil as module_0
import ssl as module_1

class Test_Netutil_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = 2453
        list_0 = module_0.bind_sockets(int_0)

if __name__ == "__main__":
    unittest.main()
