import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -3473
            h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
            str_0 = h_t_t_p_client_error_0.__str__()
            str_1 = ''
            dict_0 = {str_1: str_1}
            h_t_t_p_client_0 = module_0.HTTPClient()
            h_t_t_p_client_0.__del__()
            h_t_t_p_client_1 = module_0.HTTPClient(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
