import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            int_0 = 1411
            var_0 = module_0.check_type_int(int_0)
            bytes_0 = None
            var_1 = module_0.check_type_bool(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
