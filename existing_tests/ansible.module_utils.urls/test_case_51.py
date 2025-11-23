import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_52(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = -1400
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(int_0)
        float_0 = 102.5579
        list_0 = [unix_h_t_t_p_s_connection_0, float_0, int_0, unix_h_t_t_p_s_connection_0]
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(list_0)
        list_1 = [unix_h_t_t_p_connection_0, float_0]
        float_1 = 2159.67844
        var_0 = module_0.basic_auth_header(list_1, float_1)

if __name__ == "__main__":
    unittest.main()
