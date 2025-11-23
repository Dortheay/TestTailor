import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            float_0 = 16.267894726549905
            str_0 = None
            bytes_0 = b'\xb4s\x06\xe3\xab\x91bw\xc0\xb0\x11L\x19#\x1f'
            no_s_s_l_error_0 = module_0.NoSSLError()
            bool_0 = False
            proxy_error_0 = module_0.ProxyError()
            set_0 = {bytes_0, str_0, str_0, float_0}
            list_0 = []
            connection_error_0 = module_0.ConnectionError(*list_0)
            dict_0 = {}
            str_1 = ']`'
            str_2 = 'Darwin'
            var_0 = module_0.open_url(bool_0, set_0, dict_0, str_1, str_2, dict_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
