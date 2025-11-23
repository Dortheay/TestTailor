import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = 'S|b\x0c]#nC\\}'
            var_0 = module_0.check_type_bits(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
