import unittest
import timeout_decorator
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

class Test_Netutil_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'Estonian'
            socket_0 = module_0.bind_unix_socket(str_0)
            str_1 = ''
            dict_0 = {}
            s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
            dict_1 = {str_1: str_1, str_1: str_1, str_1: str_1, str_1: str_1}
            executor_resolver_0 = module_0.ExecutorResolver(**dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
