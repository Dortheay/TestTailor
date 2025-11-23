import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            str_0 = 'K2~B=Mt\x0cwJ+,e'
            list_0 = [str_0]
            list_1 = [list_0]
            float_0 = 942.8095
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(float_0)
            request_with_method_0 = module_0.RequestWithMethod(str_0, list_0, list_1, unix_h_t_t_p_s_connection_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
