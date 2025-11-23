import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -1306.7
            var_0 = module_0.rate_limit_argument_spec(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
