import unittest
import timeout_decorator
import sanic.response as module_0
import sanic.compat as module_1

class Test_Response_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'X(=Txm'
            h_t_t_p_response_0 = module_0.json(str_0)
            h_t_t_p_response_1 = module_0.html(str_0)
            int_0 = -896
            str_1 = 'enabled'
            callable_0 = None
            dict_0 = {str_1: str_0}
            var_0 = module_0.stream(callable_0, int_0, dict_0)
            str_2 = 'F<#XMXAZ\x0c]8R/f'
            bool_0 = True
            h_t_t_p_response_2 = module_0.empty(bool_0, dict_0)
            h_t_t_p_response_3 = module_0.text(str_1, int_0)
            str_3 = None
            h_t_t_p_response_4 = module_0.text(str_3, dict_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
