import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_79(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        var_0 = None
        str_0 = 'state'
        str_1 = 'path'
        str_2 = 'present'
        str_3 = '/example'
        str_4 = {str_0: str_2, str_1: str_3}
        var_1 = module_0.check_required_if(var_0, str_4)
        bool_0 = True
        var_2 = [str_0, str_2, str_4, bool_0]
        var_3 = [var_2]
        str_5 = {str_0: str_2}
        bool_1 = False
        var_4 = module_0.check_type_int(bool_1)
        var_5 = module_0.check_required_if(var_3, str_5)

if __name__ == "__main__":
    unittest.main()
