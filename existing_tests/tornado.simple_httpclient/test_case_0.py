import unittest
import timeout_decorator
import tornado.netutil as module_0
import tornado.tcpclient as module_1
import tornado.simple_httpclient as module_2

class Test_Simple_httpclient_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            resolver_0 = module_0.Resolver()
            t_c_p_client_0 = module_1.TCPClient(resolver_0)
            int_0 = -1810
            int_1 = -3374
            str_0 = 'tornado.simple_httpclient'
            h_t_t_p_timeout_error_0 = module_2.HTTPTimeoutError(str_0)
            set_0 = {int_1, h_t_t_p_timeout_error_0}
            h_t_t_p_request_0 = None
            float_0 = -1622.80398
            bytes_0 = b'a\x9d\xb7(\xa5h8"\xe39\x92\x90|\x046\x95'
            int_2 = 126
            int_3 = None
            h_t_t_p_connection_0 = module_2._HTTPConnection(set_0, h_t_t_p_request_0, float_0, bytes_0, int_0, t_c_p_client_0, int_2, int_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
