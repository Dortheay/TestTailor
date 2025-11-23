import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_35(self):
        try:
            bool_0 = True
            list_0 = [bool_0]
            no_s_s_l_error_0 = module_0.NoSSLError()
            unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(no_s_s_l_error_0)
            var_0 = unix_h_t_t_p_connection_0.__call__(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
