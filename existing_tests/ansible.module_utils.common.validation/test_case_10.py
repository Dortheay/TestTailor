import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            float_0 = -1382.7
            var_0 = module_0.check_type_list(float_0)
            str_0 = '7"I{lMjU"Vc'
            var_1 = module_0.check_type_float(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
