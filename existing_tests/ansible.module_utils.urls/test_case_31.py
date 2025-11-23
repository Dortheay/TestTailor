import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            proxy_error_0 = module_0.ProxyError()
            dict_0 = {proxy_error_0: proxy_error_0, proxy_error_0: proxy_error_0}
            var_0 = module_0.prepare_multipart(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
