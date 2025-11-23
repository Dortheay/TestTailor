import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            h_t_t_p_headers_0 = module_1.HTTPHeaders()
            float_0 = 1662.013136
            iterator_0 = h_t_t_p_headers_0.__iter__()
            h_t_t_p_request_0 = None
            int_0 = 1571
            str_0 = '\\}8\rFZ\n'
            str_1 = 'mgA;BZ]'
            h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, str_0, str_1, float_0)
            h_t_t_p_client_0 = module_0.HTTPClient(iterator_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
