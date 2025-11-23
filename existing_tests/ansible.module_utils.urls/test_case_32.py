import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        try:
            int_0 = None
            no_s_s_l_error_0 = module_0.NoSSLError()
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(no_s_s_l_error_0, int_0)
            var_0 = s_s_l_validation_handler_0.get_ca_certs()
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            connection_error_0 = module_0.ConnectionError()
            list_0 = [s_s_l_validation_error_0, var_0, var_0]
            var_1 = module_0.generic_urlparse(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
