import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            list_0 = []
            s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
            int_0 = -878
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(s_s_l_validation_error_0, int_0)
            int_1 = 701
            unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(int_1)
            set_0 = {s_s_l_validation_error_0}
            connection_error_0 = module_0.ConnectionError()
            request_0 = module_0.Request(h_t_t_p_s_client_auth_handler_0, unix_h_t_t_p_handler_0, set_0, connection_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
