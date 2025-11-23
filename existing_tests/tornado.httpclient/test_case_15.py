import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '\x0bowx19z)2M+m7h8'
            str_1 = '&8fR?m#\tBz\x0bz*'
            bool_0 = True
            str_2 = 'tornado.httpclient'
            iterator_0 = None
            optional_0 = None
            h_t_t_p_request_0 = module_0.HTTPRequest(str_2, iterator_0, optional_0, str_0, bool_0, bool_0, bool_0)
            list_0 = [str_2, str_1]
            h_t_t_p_client_0 = module_0.HTTPClient(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
