import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            h_t_t_p_client_0 = module_0.HTTPClient()
            h_t_t_p_client_0.__del__()
            h_t_t_p_client_0.close()
            str_0 = '0)Hyh!v9ppK5!q2EWwq'
            str_1 = '^w{c0sdu3%M'
            str_2 = '00|V3C[eq,\x0b?t2=d^m'
            dict_0 = {str_1: str_0, str_0: str_1, str_2: str_1}
            h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
