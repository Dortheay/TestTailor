import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        try:
            proxy_error_0 = module_0.ProxyError()
            str_0 = 'Darwin'
            str_1 = 'Q.@B[Z\x0c!Otx'
            str_2 = 'e#~VXVM-[wiV='
            dict_0 = {str_0: str_0, str_1: str_0, str_2: str_1, str_2: str_2}
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(dict_0)
            var_0 = unix_h_t_t_p_s_connection_0.connect()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
