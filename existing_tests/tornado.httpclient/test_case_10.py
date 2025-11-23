import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            h_t_t_p_client_0 = module_0.HTTPClient()
            h_t_t_p_request_0 = None
            int_0 = -2053
            bool_0 = True
            h_t_t_p_client_0.__del__()
            optional_0 = None
            h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, bool_0, optional_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
