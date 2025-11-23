import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = "w\x0c'xOlt+$tfP?Z\x0c"
            var_0 = module_0.check_type_list(str_0)
            int_0 = 1972
            tuple_0 = (int_0,)
            str_1 = 'ew*'
            var_1 = module_0.check_required_arguments(tuple_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
