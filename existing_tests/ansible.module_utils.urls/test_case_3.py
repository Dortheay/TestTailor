import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()
            custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler(h_t_t_p_s_client_auth_handler_0)
            var_0 = module_0.generic_urlparse(custom_h_t_t_p_s_handler_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
