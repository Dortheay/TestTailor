import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            s_s_l_context_0 = None
            s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
