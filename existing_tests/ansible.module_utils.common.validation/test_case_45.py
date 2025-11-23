import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_45(self):
        try:
            str_0 = 'arg1'
            str_1 = 'arg2'
            str_2 = 'required'
            bool_0 = True
            bool_1 = {str_2: bool_0}
            bool_2 = False
            bool_3 = {str_2: bool_2}
            bool_4 = {str_0: bool_1, str_1: bool_3}
            str_3 = 'value1'
            str_4 = 'value2'
            str_5 = {str_0: str_3, str_1: str_4}
            var_0 = module_0.check_required_arguments(bool_4, str_5)
            bool_5 = {str_2: bool_0}
            bool_6 = {str_2: bool_0}
            bool_7 = {str_0: bool_5, str_1: bool_6}
            str_6 = {str_0: str_3}
            var_1 = module_0.check_required_arguments(bool_7, str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
