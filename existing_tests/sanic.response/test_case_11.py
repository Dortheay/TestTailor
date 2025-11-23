import unittest
import timeout_decorator
import sanic.response as module_0

class Test_Response_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        h_t_m_l_protocol_0 = None
        h_t_t_p_response_0 = module_0.html(h_t_m_l_protocol_0)
        str_0 = 'W(ZhH'
        h_t_t_p_response_1 = module_0.text(str_0)

if __name__ == "__main__":
    unittest.main()
