import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            bool_0 = True
            float_0 = None
            no_s_s_l_error_0 = None
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(float_0, no_s_s_l_error_0)
            var_0 = module_0.generic_urlparse(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
