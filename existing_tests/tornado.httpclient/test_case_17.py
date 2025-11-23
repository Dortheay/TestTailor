import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'Q<F#*Ke][+'
            float_0 = 2132.83
            none_type_0 = None
            h_t_t_p_headers_0 = module_1.HTTPHeaders()
            int_0 = 200
            bool_0 = True
            set_0 = None
            bytes_0 = b'X\xeb\xcf\x8e\x98&\xa1\xa7\xcbTL\xdb\x0f\xc7Q\xb9o\x81\xa1'
            list_0 = [int_0, bytes_0, str_0]
            h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, float_0, none_type_0, str_0, h_t_t_p_headers_0, str_0, int_0, bool_0, set_0, list_0)
            dict_0 = {str_0: set_0, str_0: list_0}
            request_proxy_0 = module_0._RequestProxy(h_t_t_p_request_0, dict_0)
            str_1 = '\x0bowx19z)2M+m7h8'
            int_1 = -4263
            bool_1 = True
            iterator_0 = None
            optional_0 = None
            h_t_t_p_request_1 = module_0.HTTPRequest(str_1, iterator_0, optional_0, str_1, bool_1, bool_1, bool_1)
            h_t_t_p_headers_1 = module_1.HTTPHeaders()
            list_1 = None
            h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_1, int_1, h_t_t_p_headers_1, list_1)
            str_2 = h_t_t_p_response_0.__repr__()
            module_0.main()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
