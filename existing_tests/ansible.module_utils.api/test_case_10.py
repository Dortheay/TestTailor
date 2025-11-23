import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        var_0 = module_0.basic_auth_argument_spec()

if __name__ == "__main__":
    unittest.main()
