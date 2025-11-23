import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            int_0 = 2392
            var_0 = module_0.check_type_list(int_0)
            bytes_0 = b'\xf7\xc6'
            bytes_1 = b's\xe5\x9f\xa7]|@'
            var_1 = module_0.check_required_by(bytes_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
