import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()
            str_0 = 'percent'
            var_0 = h_t_t_p_s_client_auth_handler_0.https_open(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
