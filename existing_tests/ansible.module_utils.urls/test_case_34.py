import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        try:
            proxy_error_0 = module_0.ProxyError()
            dict_0 = {proxy_error_0: proxy_error_0, proxy_error_0: proxy_error_0}
            str_0 = 'r\t['
            unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(str_0)
            list_0 = [unix_h_t_t_p_connection_0, unix_h_t_t_p_connection_0]
            s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
            tuple_0 = (s_s_l_validation_error_0,)
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(tuple_0)
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(h_t_t_p_s_client_auth_handler_0)
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(unix_h_t_t_p_connection_0, dict_0, unix_h_t_t_p_s_connection_0)
            connection_error_0 = module_0.ConnectionError(*list_0)
            missing_module_error_0 = module_0.MissingModuleError(dict_0, connection_error_0)
            var_0 = module_0.fetch_file(s_s_l_validation_handler_0, h_t_t_p_s_client_auth_handler_0, missing_module_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
