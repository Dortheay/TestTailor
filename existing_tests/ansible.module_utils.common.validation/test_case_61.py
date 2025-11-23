import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_62(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        int_0 = 3
        var_0 = module_0.check_type_int(int_0)

if __name__ == "__main__":
    unittest.main()
