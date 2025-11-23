import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_48(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_47(self):
        try:
            var_0 = None
            str_0 = 'state'
            str_1 = 'path'
            str_2 = 'present'
            str_3 = '/example'
            str_4 = {str_0: str_2, str_1: str_3}
            var_1 = module_0.check_required_if(var_0, str_4)
            bool_0 = False
            str_5 = (str_1,)
            var_2 = [str_1, str_2, str_5, bool_0]
            var_3 = [var_2]
            str_6 = {str_0: str_2, str_1: str_3}
            var_4 = module_0.check_required_if(var_3, str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
