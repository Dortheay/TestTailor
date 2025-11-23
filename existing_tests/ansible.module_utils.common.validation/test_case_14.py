import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            bool_0 = True
            var_0 = module_0.check_type_bool(bool_0)
            list_0 = []
            tuple_0 = None
            var_1 = module_0.check_required_if(list_0, tuple_0)
            str_0 = None
            var_2 = module_0.check_type_jsonarg(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
