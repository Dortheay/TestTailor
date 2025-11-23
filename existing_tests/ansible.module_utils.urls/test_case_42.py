import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_42(self):
        try:
            list_0 = []
            request_0 = module_0.Request(list_0)
            list_1 = []
            custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
            dict_0 = {}
            proxy_error_0 = module_0.ProxyError(*list_1, **dict_0)
            custom_h_t_t_p_s_handler_1 = module_0.CustomHTTPSHandler(custom_h_t_t_p_s_handler_0, proxy_error_0)
            var_0 = request_0.delete(custom_h_t_t_p_s_handler_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
