import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            list_0 = [bool_0, bool_0, bool_0]
            dict_0 = {}
            no_s_s_l_error_0 = module_0.NoSSLError(*list_0, **dict_0)
            proxy_error_0 = module_0.ProxyError()
            unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(proxy_error_0, **dict_0)
            missing_module_error_0 = module_0.MissingModuleError(no_s_s_l_error_0, unix_h_t_t_p_handler_0)
            var_0 = module_0.generic_urlparse(missing_module_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
