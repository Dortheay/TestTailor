import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'BKG=\x0bCmAy!]qM'
            str_1 = 'E)D\nD'
            validation_result_0 = module_0.ValidationResult(str_1)
            argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_0, str_0, validation_result_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
