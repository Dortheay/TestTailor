import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        int_0 = 2933
        var_0 = module_0.retry_never(int_0)

if __name__ == "__main__":
    unittest.main()
