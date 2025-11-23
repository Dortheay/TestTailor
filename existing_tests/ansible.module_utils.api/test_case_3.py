import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 512.0
            set_0 = {float_0, float_0}
            var_0 = module_0.retry_with_delays_and_condition(set_0)
            int_0 = 1906
            var_1 = module_0.basic_auth_argument_spec(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
