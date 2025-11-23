import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.retry()

if __name__ == "__main__":
    unittest.main()
