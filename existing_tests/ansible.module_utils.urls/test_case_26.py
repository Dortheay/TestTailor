import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
            proxy_error_0 = module_0.ProxyError()
            str_0 = 'comment'
            set_0 = set()
            str_1 = '(p\x0b?~z}d G\n"G2!Ms-a'
            var_0 = module_0.build_ssl_validation_error(proxy_error_0, str_0, set_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
