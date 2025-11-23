import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_49(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_48(self):
        try:
            str_0 = 'state'
            str_1 = 'present'
            str_2 = '/example'
            bool_0 = True
            var_0 = [str_0, str_1, str_2, bool_0]
            var_1 = [var_0]
            str_3 = {str_0: str_1}
            bool_1 = False
            var_2 = module_0.check_type_int(bool_1)
            var_3 = module_0.check_required_if(var_1, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
