import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = 450
        var_0 = module_0.rate_limit()
        bool_0 = True
        var_1 = module_0.retry_never(bool_0)
        var_2 = module_0.rate_limit(int_0)
        dict_0 = {var_0: var_0}
        var_3 = module_0.retry_argument_spec(dict_0)

if __name__ == "__main__":
    unittest.main()
