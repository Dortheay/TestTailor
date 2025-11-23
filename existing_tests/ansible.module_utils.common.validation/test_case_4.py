import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = 1.5
            str_0 = '5(hZ|_:7'
            var_0 = module_0.check_missing_parameters(float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
