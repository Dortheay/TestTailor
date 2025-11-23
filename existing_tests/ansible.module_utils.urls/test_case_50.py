import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_51(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        list_0 = []
        request_0 = module_0.Request(list_0)
        bytes_0 = b'\xf5B\x9a'
        bool_0 = False
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(request_0, bytes_0, bool_0)

if __name__ == "__main__":
    unittest.main()
