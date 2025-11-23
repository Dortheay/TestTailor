import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_38(self):
        try:
            float_0 = None
            str_0 = '|\x0b&u^m'
            var_0 = module_0.check_mutually_exclusive(str_0, str_0)
            int_0 = -4287
            var_1 = module_0.safe_eval(int_0)
            str_1 = None
            bool_0 = True
            var_2 = module_0.check_required_by(str_1, bool_0)
            var_3 = module_0.check_type_dict(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
