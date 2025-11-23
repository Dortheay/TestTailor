import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_36(self):
        try:
            proxy_error_0 = module_0.ProxyError()
            str_0 = '0du25Y0zTK*6`#pO\n'
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()
            dict_0 = {str_0: proxy_error_0}
            tuple_0 = (str_0, str_0, h_t_t_p_s_client_auth_handler_0, dict_0)
            unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(tuple_0)
            str_1 = 'LV8Ij'
            str_2 = '<nT@9a7'
            dict_1 = {str_1: proxy_error_0, str_2: proxy_error_0}
            parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_1)
            bool_0 = True
            tuple_1 = (parse_result_dotted_dict_0, bool_0, dict_1)
            set_0 = set()
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(tuple_1, set_0)
            var_0 = s_s_l_validation_handler_0.http_request(unix_h_t_t_p_handler_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
