import unittest
import timeout_decorator
import httpie.models as module_0

class Test_Models_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = 663
            h_t_t_p_request_0 = module_0.HTTPRequest(int_0)
            h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0)
            h_t_t_p_response_1 = module_0.HTTPResponse(h_t_t_p_response_0)
            var_0 = h_t_t_p_response_1.iter_body()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
