import unittest
import timeout_decorator
import sanic.response as module_0
import sanic.compat as module_1

class Test_Response_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            h_t_m_l_protocol_0 = None
            h_t_t_p_response_0 = module_0.html(h_t_m_l_protocol_0)
            str_0 = '|Ba'
            int_0 = -2848
            callable_0 = None
            set_0 = {callable_0, int_0}
            var_0 = module_0.stream(callable_0, str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
