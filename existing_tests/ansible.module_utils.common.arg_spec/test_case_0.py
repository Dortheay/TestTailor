import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
