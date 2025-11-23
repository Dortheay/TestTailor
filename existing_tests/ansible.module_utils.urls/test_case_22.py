import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            bool_0 = True
            unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(bool_0)
            str_0 = '!<?'
            missing_module_error_0 = module_0.MissingModuleError(unix_h_t_t_p_handler_0, str_0)
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            set_0 = {s_s_l_validation_error_0, missing_module_error_0}
            custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler(set_0)
            list_0 = [unix_h_t_t_p_handler_0, custom_h_t_t_p_s_handler_0, str_0]
            var_0 = unix_h_t_t_p_handler_0.http_open(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
