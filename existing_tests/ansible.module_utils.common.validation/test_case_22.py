import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            int_0 = 944
            var_0 = module_0.check_type_bytes(int_0)
            var_1 = module_0.check_type_bytes(int_0)
            set_0 = None
            var_2 = module_0.check_type_float(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
