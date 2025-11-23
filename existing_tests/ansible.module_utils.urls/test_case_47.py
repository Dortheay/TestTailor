import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_48(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_47(self):
        try:
            int_0 = None
            no_s_s_l_error_0 = module_0.NoSSLError()
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(no_s_s_l_error_0, int_0)
            var_0 = s_s_l_validation_handler_0.get_ca_certs()
            var_1 = s_s_l_validation_handler_0.detect_no_proxy(int_0)
            var_2 = s_s_l_validation_handler_0.get_ca_certs()
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            h_t_t_p_s_client_auth_handler_0 = None
            bool_0 = True
            var_3 = s_s_l_validation_handler_0.make_context(h_t_t_p_s_client_auth_handler_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
