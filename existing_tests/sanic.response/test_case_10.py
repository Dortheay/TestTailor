import unittest
import timeout_decorator
import sanic.response as module_0

class Test_Response_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'X(=Txm'
        h_t_t_p_response_0 = module_0.html(str_0)
        int_0 = -900
        h_t_t_p_response_1 = module_0.json(str_0, int_0)

if __name__ == "__main__":
    unittest.main()
