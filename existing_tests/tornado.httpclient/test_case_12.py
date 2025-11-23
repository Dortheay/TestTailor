import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'yV3'
            str_1 = 'tornado.httpclient'
            int_0 = 3043
            h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
            str_2 = h_t_t_p_client_error_0.__str__()
            dict_0 = {str_0: str_0, str_1: str_1}
            async_h_t_t_p_client_0 = module_0.AsyncHTTPClient(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
