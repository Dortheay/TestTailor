import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            tuple_0 = ()
            var_0 = module_0.RedirectHandlerFactory(tuple_0)
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(s_s_l_validation_error_0)
            var_1 = unix_h_t_t_p_s_connection_0.__call__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
