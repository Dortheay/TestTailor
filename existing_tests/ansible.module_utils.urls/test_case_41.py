import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_41(self):
        try:
            var_0 = module_0.url_argument_spec()
            dict_0 = {}
            int_0 = None
            no_s_s_l_error_0 = module_0.NoSSLError()
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(no_s_s_l_error_0, int_0)
            var_1 = s_s_l_validation_handler_0.get_ca_certs()
            connection_error_0 = module_0.ConnectionError()
            var_2 = module_0.prepare_multipart(dict_0)
            tuple_0 = ()
            str_0 = "/usr/contrib/bin/machinfo | grep Intel |cut -d' ' -f4-"
            var_3 = s_s_l_validation_handler_0.validate_proxy_response(str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
