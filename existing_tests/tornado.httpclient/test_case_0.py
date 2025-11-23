import unittest
import timeout_decorator
import tornado.httpclient as module_0

class Test_Httpclient_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        h_t_t_p_client_0 = module_0.HTTPClient()

if __name__ == "__main__":
    unittest.main()
