import unittest
import timeout_decorator
import tornado.httpclient as module_0

class Test_Httpclient_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'http://example.com'
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0)
        int_0 = 200
        var_0 = None
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, var_0)

if __name__ == "__main__":
    unittest.main()
