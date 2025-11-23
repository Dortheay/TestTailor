import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
            str_0 = 'failed fuzzy extension match for {0} in {1}'
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            custom_h_t_t_p_s_handler_1 = module_0.CustomHTTPSHandler(s_s_l_validation_error_0)
            var_0 = custom_h_t_t_p_s_handler_1.https_open(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
