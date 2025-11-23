import unittest
import timeout_decorator
import tornado.simple_httpclient as module_0

class Test_Simple_httpclient_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'Qc'
        h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
        str_1 = h_t_t_p_stream_closed_error_0.__str__()

if __name__ == "__main__":
    unittest.main()
