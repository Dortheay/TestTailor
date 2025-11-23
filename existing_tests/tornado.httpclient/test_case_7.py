import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'lP9 vrt9^+J:8\\^0^^'
            h_t_t_p_client_0 = module_0.HTTPClient()
            h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
