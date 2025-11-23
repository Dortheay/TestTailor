import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_52(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '---'
        var_0 = module_0.check_missing_parameters(str_0)

if __name__ == "__main__":
    unittest.main()
