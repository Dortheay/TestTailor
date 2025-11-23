import unittest
import timeout_decorator
import tornado.httpclient as module_0

class Test_Httpclient_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'http://example.com'
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0)

if __name__ == "__main__":
    unittest.main()
