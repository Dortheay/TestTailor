import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -2992.69379
            var_0 = module_0.count_terms(float_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
