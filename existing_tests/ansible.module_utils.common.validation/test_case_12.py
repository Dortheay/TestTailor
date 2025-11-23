import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            float_0 = None
            var_0 = module_0.check_type_dict(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
