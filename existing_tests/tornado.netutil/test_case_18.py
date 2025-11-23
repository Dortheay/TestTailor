import unittest
import timeout_decorator
import tornado.netutil as module_0
import ssl as module_1

class Test_Netutil_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()

if __name__ == "__main__":
    unittest.main()
