import unittest
import timeout_decorator
import tornado.simple_httpclient as module_0

class Test_Simple_httpclient_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '&o'
        h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)
        str_1 = h_t_t_p_timeout_error_0.__str__()

if __name__ == "__main__":
    unittest.main()
