import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            bool_0 = False
            list_0 = []
            request_0 = module_0.Request(list_0)
            bytes_0 = b'\xf5B\x9a'
            bool_1 = False
            s_s_l_validation_handler_0 = module_0.SSLValidationHandler(request_0, bytes_0, bool_1)
            var_0 = s_s_l_validation_handler_0.validate_proxy_response(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
