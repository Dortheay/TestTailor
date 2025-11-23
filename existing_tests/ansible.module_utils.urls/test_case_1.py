import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            custom_h_t_t_p_s_connection_0 = module_0.CustomHTTPSConnection()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
