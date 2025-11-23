import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_71(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        str_0 = 'path'
        str_1 = 'present'
        str_2 = '/example'
        str_3 = {str_0: str_1, str_0: str_2}
        bool_0 = False
        var_0 = [str_1, str_1, str_3, bool_0]
        var_1 = [var_0]
        str_4 = {str_0: str_1}
        var_2 = module_0.check_required_if(var_1, str_4)

if __name__ == "__main__":
    unittest.main()
