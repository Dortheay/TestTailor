import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_37(self):
        try:
            str_0 = 'H~A>q[\r]B t'
            var_0 = module_0.generic_urlparse(str_0)
            str_1 = ''
            dict_0 = {str_1: str_0}
            no_s_s_l_error_0 = module_0.NoSSLError()
            int_0 = 5985
            unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(int_0)
            dict_1 = {str_1: str_1, str_1: dict_0, str_0: int_0}
            custom_h_t_t_p_s_connection_0 = module_0.CustomHTTPSConnection(**dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
