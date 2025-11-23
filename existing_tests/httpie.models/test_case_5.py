import unittest
import timeout_decorator
import httpie.models as module_0

class Test_Models_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 2685.08317
        h_t_t_p_request_0 = module_0.HTTPRequest(float_0)

if __name__ == "__main__":
    unittest.main()
