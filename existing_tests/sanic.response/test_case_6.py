import unittest
import timeout_decorator
import sanic.response as module_0
import sanic.compat as module_1

class Test_Response_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'X(=Txm'
            str_1 = None
            h_t_t_p_response_0 = module_0.html(str_1)
            int_0 = -900
            str_2 = 'enabled'
            callable_0 = None
            dict_0 = {str_2: str_0}
            str_3 = '.o@\'>"Z'
            h_t_t_p_response_1 = module_0.empty(str_3)
            base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
            str_4 = 'QI8$4'
            dict_1 = {str_2: h_t_t_p_response_1}
            var_0 = module_0.stream(callable_0, int_0, dict_0, str_4, dict_1)
            bytes_0 = b'\x0c\xf9\x82\x18\x9eg\xaac'
            h_t_t_p_response_2 = module_0.empty(bytes_0)
            dict_2 = None
            header_0 = module_1.Header(**dict_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
