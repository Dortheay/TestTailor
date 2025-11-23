import unittest
import timeout_decorator
import tornado.httpclient as module_0
import tornado.httputil as module_1

class Test_Httpclient_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'He02`5~=<uSFe<F-HHdR'
            bool_0 = True
            int_0 = -2773
            str_1 = ''
            h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, bool_0, int_0, bool_0, str_1, str_0, int_0, str_0, str_0, bool_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
