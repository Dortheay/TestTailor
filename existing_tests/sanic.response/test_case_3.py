import unittest
import timeout_decorator
import sanic.response as module_0
import sanic.compat as module_1

class Test_Response_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = "h]R<9jk(g&K'S~M;j8v"
            dict_0 = {}
            h_t_t_p_response_0 = module_0.redirect(str_0, dict_0)
            str_1 = "\\ACV'_@=}!\x0cN{D"
            int_0 = 1000
            h_t_t_p_response_1 = module_0.redirect(str_1, int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
