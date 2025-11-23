import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_67(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        str_0 = 'o>t`J&tJa\r=i\\\x0c!sOU'
        var_0 = module_0.check_type_dict(str_0)

if __name__ == "__main__":
    unittest.main()
