import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_47(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_46(self):
        try:
            list_0 = []
            request_0 = module_0.Request(list_0)
            dict_0 = None
            unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(dict_0)
            var_0 = request_0.patch(unix_h_t_t_p_connection_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
