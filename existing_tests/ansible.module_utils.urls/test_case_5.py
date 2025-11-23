import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 125
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(int_0)
            bytes_0 = b'\x9b\xc7'
            var_0 = module_0.generic_urlparse(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
