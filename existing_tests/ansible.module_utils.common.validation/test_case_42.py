import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_42(self):
        try:
            str_0 = 'f2\'D&a\n}"/*m'
            bytes_0 = b'\x86\x8d'
            tuple_0 = (bytes_0,)
            set_0 = {tuple_0, str_0, tuple_0, tuple_0}
            var_0 = module_0.check_required_together(tuple_0, set_0)
            var_1 = module_0.check_type_jsonarg(str_0)
            dict_0 = {bytes_0: var_1}
            list_0 = []
            var_2 = module_0.check_required_by(dict_0, set_0, list_0)
            str_1 = ' Set CLI options depending on params '
            float_0 = 1000.0
            var_3 = module_0.check_required_one_of(set_0, str_1, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
