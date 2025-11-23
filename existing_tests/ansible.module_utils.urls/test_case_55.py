import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_56(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        no_s_s_l_error_0 = module_0.NoSSLError()
        bool_0 = True
        var_0 = module_0.atexit_remove_file(bool_0)
        proxy_error_0 = module_0.ProxyError()
        no_s_s_l_error_1 = module_0.NoSSLError()
        proxy_error_1 = module_0.ProxyError()

if __name__ == "__main__":
    unittest.main()
