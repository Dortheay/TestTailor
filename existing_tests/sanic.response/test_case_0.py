import unittest
import timeout_decorator
import sanic.response as module_0
import sanic.compat as module_1

class Test_Response_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            h_t_t_p_response_0 = module_0.empty()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
