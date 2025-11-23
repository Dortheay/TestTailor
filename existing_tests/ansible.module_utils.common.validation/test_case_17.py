import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = 'o>t`J&tJa=i\x0c!sOU'
            var_0 = module_0.check_type_float(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
