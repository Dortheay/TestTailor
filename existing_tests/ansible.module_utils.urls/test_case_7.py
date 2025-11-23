import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            proxy_error_0 = module_0.ProxyError()
            int_0 = 309
            list_0 = [proxy_error_0, int_0, int_0, int_0]
            unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(list_0)
            var_0 = unix_h_t_t_p_connection_0.connect()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
