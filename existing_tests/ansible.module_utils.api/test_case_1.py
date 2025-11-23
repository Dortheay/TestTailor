import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 1906
            var_0 = module_0.basic_auth_argument_spec(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
