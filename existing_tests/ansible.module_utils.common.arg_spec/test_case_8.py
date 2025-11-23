import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        dict_0 = {}
        str_0 = '%j`:wMR .8? 7zLE`'
        str_1 = 'K;H(ZXZCQ8DJ:`F%'
        dict_1 = {str_1: dict_0}
        list_0 = [dict_0, str_0]
        module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
        var_0 = module_argument_spec_validator_0.validate(dict_1)

if __name__ == "__main__":
    unittest.main()
