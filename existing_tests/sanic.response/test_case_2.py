import unittest
import timeout_decorator
import sanic.response as module_0
import sanic.compat as module_1

class Test_Response_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '\r/zuM>k;6 l%E'
            streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(str_0)
            var_0 = None
            dict_0 = {str_0: str_0, str_0: streaming_h_t_t_p_response_0, str_0: str_0}
            h_t_t_p_response_0 = module_0.file(str_0, var_0)
            var_1 = streaming_h_t_t_p_response_0.send()
            var_2 = streaming_h_t_t_p_response_0.send(**dict_0)
            h_t_t_p_response_1 = module_0.raw(var_0)
            str_1 = 'R^Mw|'
            int_0 = 300
            var_3 = streaming_h_t_t_p_response_0.send()
            h_t_t_p_response_2 = module_0.redirect(str_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
