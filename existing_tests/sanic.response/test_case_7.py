import unittest
import timeout_decorator
import sanic.response as module_0

class Test_Response_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        h_t_t_p_response_0 = module_0.HTTPResponse()

if __name__ == "__main__":
    unittest.main()
