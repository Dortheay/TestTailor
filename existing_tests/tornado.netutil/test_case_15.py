import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = None
            int_0 = -326
            address_family_0 = None
            resolver_0 = module_0.Resolver()
            list_0 = [resolver_0, resolver_0]
            override_resolver_0 = module_0.OverrideResolver(*list_0)
            awaitable_0 = override_resolver_0.resolve(str_0, int_0, address_family_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
