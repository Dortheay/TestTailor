import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        try:
            int_0 = -98
            str_0 = '34>@+n0JI[a\x0b'
            var_0 = module_0.check_type_raw(str_0)
            list_0 = [int_0, int_0, int_0]
            var_1 = module_0.check_type_list(list_0)
            list_1 = []
            tuple_0 = None
            var_2 = module_0.check_required_if(list_1, tuple_0)
            str_1 = None
            var_3 = module_0.check_type_dict(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
