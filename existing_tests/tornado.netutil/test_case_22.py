import unittest
import timeout_decorator
import tornado.netutil as module_0
import ssl as module_1

class Test_Netutil_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        resolver_0 = module_0.Resolver()
        resolver_0.close()

if __name__ == "__main__":
    unittest.main()
