import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = 1039
            var_0 = module_0.check_type_bool(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
