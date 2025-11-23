import unittest
import timeout_decorator
import httpie.models as module_0

class Test_Models_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = True
            set_0 = {bool_0, bool_0}
            set_1 = set()
            h_t_t_p_response_0 = module_0.HTTPResponse(set_1)
            var_0 = h_t_t_p_response_0.iter_lines(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
