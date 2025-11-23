import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_36(self):
        try:
            float_0 = None
            str_0 = '|:Y1Y|a(mxwodj2aR'
            float_1 = 0.001
            set_0 = {float_1}
            var_0 = module_0.count_terms(float_1, set_0)
            dict_0 = {str_0: float_0}
            set_1 = {str_0, var_0, float_0}
            var_1 = module_0.check_required_by(dict_0, set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
