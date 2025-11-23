import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_47(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_46(self):
        try:
            var_0 = None
            str_0 = 'key1'
            str_1 = 'value1'
            str_2 = [str_1]
            str_3 = {str_0: str_2}
            str_4 = 'value2'
            str_5 = {str_0: str_3}
            str_6 = 'something'
            str_7 = 'val1'
            str_8 = 'val2'
            str_9 = {str_0: str_6, str_1: str_7, str_4: str_8}
            dict_0 = None
            int_0 = 69
            var_1 = module_0.check_mutually_exclusive(dict_0, int_0)
            var_2 = module_0.check_required_by(str_5, str_9)
            str_10 = [str_1, str_4]
            str_11 = {str_0: str_10}
            var_3 = {str_0: str_6, str_1: var_0}
            var_4 = module_0.check_required_by(str_11, var_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
