import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            var_0 = module_0.url_argument_spec()
            dict_0 = {}
            list_0 = [dict_0]
            dict_1 = {}
            bytes_0 = None
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(list_0)
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(s_s_l_validation_error_0)
            var_1 = module_0.open_url(list_0, dict_1, bytes_0, dict_1, dict_0, unix_h_t_t_p_s_connection_0, unix_h_t_t_p_handler_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
