import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            str_0 = 'BQ#\t*LlUOe.~]$YZ6'
            float_0 = -2548.069271
            var_0 = module_0.check_required_if(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
