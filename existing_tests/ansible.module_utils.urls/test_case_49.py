import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_50(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = None
        float_0 = -99.20110741576659
        var_0 = module_0.maybe_add_ssl_handler(int_0, float_0)

if __name__ == "__main__":
    unittest.main()
