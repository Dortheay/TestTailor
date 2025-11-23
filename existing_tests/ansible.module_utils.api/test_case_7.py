import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = module_0.rate_limit_argument_spec()

if __name__ == "__main__":
    unittest.main()
