import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_51(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_50(self):
        try:
            var_0 = None
            var_1 = {}
            var_2 = module_0.check_required_by(var_0, var_1)
            str_0 = 'key1'
            str_1 = 'value1'
            str_2 = [str_1]
            str_3 = {str_0: str_2}
            var_3 = {}
            var_4 = module_0.check_required_by(str_3, var_3)
            int_0 = -2775
            var_5 = module_0.check_type_int(int_0)
            str_4 = 'value2'
            str_5 = [str_1, str_4]
            str_6 = {str_0: str_5}
            str_7 = 'somethi\nng'
            str_8 = 'val1'
            str_9 = 'val2'
            str_10 = {str_0: str_7, str_1: str_8, str_4: str_9}
            dict_0 = None
            int_1 = 69
            float_0 = 2.0
            var_6 = module_0.check_type_float(float_0)
            var_7 = module_0.check_mutually_exclusive(dict_0, int_1)
            var_8 = module_0.check_required_by(str_6, str_10)
            str_11 = {str_0: str_8}
            var_9 = {str_0: str_7, str_1: var_0}
            var_10 = module_0.check_required_by(str_11, var_9)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
