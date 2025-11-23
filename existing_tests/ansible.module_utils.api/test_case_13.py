import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 2
        int_1 = 10
        var_0 = module_0.generate_jittered_backoff(int_0, int_0, int_1)
        var_1 = list(var_0)
        var_2 = len(var_1)

if __name__ == "__main__":
    unittest.main()
