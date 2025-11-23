import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_45(self):
        try:
            no_s_s_l_error_0 = None
            list_0 = []
            request_0 = module_0.Request(list_0)
            list_1 = []
            parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(*list_1)
            str_0 = '&'
            str_1 = '\x0cI?IM=\x0co<aJ9\x0c'
            str_2 = 'W5-yDtx315,< (~'
            dict_0 = {str_0: parse_result_dotted_dict_0, str_1: str_0, str_2: no_s_s_l_error_0, str_1: str_0}
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(dict_0)
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(str_0)
            custom_h_t_t_p_s_handler_0 = None
            missing_module_error_0 = module_0.MissingModuleError(unix_h_t_t_p_s_connection_0, custom_h_t_t_p_s_handler_0)
            str_3 = None
            str_4 = '7\'p% /N+69B\\bwxB"&H'
            no_s_s_l_error_1 = module_0.NoSSLError(*list_1)
            dict_1 = {str_3: str_3, str_4: no_s_s_l_error_1}
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(dict_1, parse_result_dotted_dict_0, s_s_l_validation_error_0)
            var_0 = s_s_l_validation_handler_0.make_context(h_t_t_p_s_client_auth_handler_0, missing_module_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
