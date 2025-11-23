import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '\x0c-\\%^9 Y'
            str_1 = "-:9:,sC' ^X"
            int_0 = 127
            h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, str_1, str_1, str_1, int_0, str_1, str_1)
            h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, str_1)
            h_t_t_p_response_0.rethrow()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
