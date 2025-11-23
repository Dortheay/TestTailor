import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = None
            address_family_0 = module_1.AddressFamily.AF_IRDA
            bool_0 = True
            list_0 = module_0.bind_sockets(int_0, address_family_0, int_0, int_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
