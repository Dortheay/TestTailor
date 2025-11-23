import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_69(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        str_0 = 'f2\'D&a\n}"/*m'
        bytes_0 = b'\x86\x8d'
        tuple_0 = (bytes_0,)
        set_0 = {tuple_0, str_0, tuple_0, tuple_0}
        var_0 = module_0.check_required_together(tuple_0, set_0)
        var_1 = module_0.check_type_jsonarg(str_0)

if __name__ == "__main__":
    unittest.main()
