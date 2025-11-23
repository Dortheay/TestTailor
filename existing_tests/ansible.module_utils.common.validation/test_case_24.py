import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            list_0 = []
            float_0 = -1860.66
            var_0 = module_0.check_required_arguments(list_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
