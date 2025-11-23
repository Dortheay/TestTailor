import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            var_0 = module_0.url_argument_spec()
            dict_0 = {}
            int_0 = None
            no_s_s_l_error_0 = module_0.NoSSLError()
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(no_s_s_l_error_0, int_0)
            var_1 = s_s_l_validation_handler_0.detect_no_proxy(int_0)
            var_2 = s_s_l_validation_handler_0.get_ca_certs()
            str_0 = '535\tnLIyN'
            dict_1 = {str_0: str_0, str_0: str_0}
            parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_1)
            custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
            connection_error_0 = module_0.ConnectionError()
            var_3 = module_0.prepare_multipart(dict_0)
            var_4 = module_0.basic_auth_header(parse_result_dotted_dict_0, int_0)
            var_5 = parse_result_dotted_dict_0.as_list()
            var_6 = module_0.generic_urlparse(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
