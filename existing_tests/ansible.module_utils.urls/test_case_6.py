import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bool_0 = True
            dict_0 = {}
            parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
            var_0 = module_0.prepare_multipart(parse_result_dotted_dict_0)
            custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
            no_s_s_l_error_0 = module_0.NoSSLError()
            int_0 = -3362
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(no_s_s_l_error_0, int_0)
            float_0 = -3076.16
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(float_0)
            list_0 = [parse_result_dotted_dict_0, bool_0, int_0]
            var_1 = unix_h_t_t_p_s_connection_0.__call__(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
