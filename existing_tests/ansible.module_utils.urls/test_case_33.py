import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            bool_0 = True
            connection_error_0 = module_0.ConnectionError()
            s_s_l_validation_error_0 = module_0.SSLValidationError()
            var_0 = module_0.build_ssl_validation_error(bool_0, connection_error_0, s_s_l_validation_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
