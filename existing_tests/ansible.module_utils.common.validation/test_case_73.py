import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_74(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        str_0 = 'f2\'D&a\n}"/*m'
        bytes_0 = b't'
        tuple_0 = (bytes_0,)
        set_0 = {tuple_0, str_0, tuple_0, tuple_0}
        var_0 = module_0.check_required_together(tuple_0, set_0)
        var_1 = module_0.check_type_jsonarg(str_0)
        str_1 = 'o%t`J&tJa=i\x0c!sOU'
        var_2 = module_0.check_type_dict(str_1)
        bytes_1 = b''
        list_0 = [var_2, bytes_0, set_0, bytes_0]
        var_3 = module_0.check_required_one_of(bytes_1, list_0)
        str_2 = '\nRIqg=/``)5o1zie-'
        str_3 = 'i+Js?Y)8'
        str_4 = "n='j;"
        var_4 = module_0.safe_eval(str_2, str_3, str_4)

if __name__ == "__main__":
    unittest.main()
