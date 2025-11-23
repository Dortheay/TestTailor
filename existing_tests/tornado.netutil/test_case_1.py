import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            resolver_0 = module_0.Resolver()
            resolver_0.close()
            default_executor_resolver_0 = module_0.DefaultExecutorResolver()
            set_0 = None
            socket_0 = module_1.socket(default_executor_resolver_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
