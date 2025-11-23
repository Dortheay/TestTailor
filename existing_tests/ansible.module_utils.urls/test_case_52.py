import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_53(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        var_0 = module_0.url_argument_spec()
        int_0 = None
        no_s_s_l_error_0 = module_0.NoSSLError()
        int_1 = 20
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(no_s_s_l_error_0, int_1)
        var_1 = s_s_l_validation_handler_0.detect_no_proxy(int_0)
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(s_s_l_validation_error_0)

if __name__ == "__main__":
    unittest.main()
