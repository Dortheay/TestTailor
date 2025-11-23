import unittest
import timeout_decorator
import tornado.httpclient as module_0

class Test_Httpclient_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_0.close()

if __name__ == "__main__":
    unittest.main()
