import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_28(self):
        try:
            bytes_0 = b'\xb4s\x06\xe3\xab\x91bw\xc0\xb0\x11L\x19#\x1f'
            no_s_s_l_error_0 = module_0.NoSSLError()
            unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(no_s_s_l_error_0)
            h_t_t_p_s_client_auth_handler_0 = None
            str_0 = '='
            bytes_1 = b'(\xcd\xf40\xe3t7[_5\xc9\xb9\x0e$'
            float_0 = -835.0
            proxy_error_0 = module_0.ProxyError()
            var_0 = module_0.open_url(bytes_0, unix_h_t_t_p_connection_0, proxy_error_0, h_t_t_p_s_client_auth_handler_0, str_0, bytes_1, proxy_error_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
