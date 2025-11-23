import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_39(self):
        try:
            var_0 = module_0.url_argument_spec()
            dict_0 = {}
            int_0 = None
            no_s_s_l_error_0 = module_0.NoSSLError()
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(no_s_s_l_error_0, int_0)
            var_1 = s_s_l_validation_handler_0.get_ca_certs()
            connection_error_0 = module_0.ConnectionError()
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(dict_0)
            bool_0 = False
            bool_1 = False
            request_0 = module_0.Request(bool_0, bool_1)
            bytes_0 = b'\xbc\xd3O.\xbb\x9ci\xdf\x05\x0bo\xe4vB\x02-'
            var_2 = request_0.options(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
