import unittest
import timeout_decorator
import sanic.response as module_0
import sanic.compat as module_1

class Test_Response_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'X(=Txm'
            str_1 = None
            h_t_t_p_response_0 = module_0.html(str_1)
            int_0 = -900
            str_2 = 'enabled'
            callable_0 = None
            dict_0 = {str_2: str_0}
            var_0 = module_0.stream(callable_0, int_0, dict_0)
            str_3 = '\\303BA\rt47'
            bool_0 = True
            h_t_t_p_response_1 = module_0.empty(bool_0, dict_0)
            base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
            str_4 = 'QI8$4'
            str_5 = 'F<#XMXAZ\x0c]8R/f'
            h_t_t_p_response_2 = module_0.empty()
            int_1 = 2674
            h_t_t_p_response_3 = module_0.redirect(str_5, dict_0)
            str_6 = '- ?>x2\\B)5\rk'
            str_7 = '`dS^'
            dict_1 = {str_3: str_1, str_4: str_6, str_7: str_4}
            h_t_t_p_response_4 = module_0.json(int_1, int_1, dict_0, str_4, h_t_t_p_response_3, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
