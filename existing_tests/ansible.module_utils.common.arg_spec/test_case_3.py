import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            tuple_0 = ()
            dict_0 = {}
            list_0 = [tuple_0, dict_0, tuple_0, dict_0]
            argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_0, list_0)
            list_1 = [dict_0, argument_spec_validator_0, argument_spec_validator_0]
            module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_1)
            str_0 = '\n    This is a generic Hostname manipulation class that is subclassed\n    based on platform.\n\n    A subclass may wish to set different strategy instance to self.strategy.\n\n    All subclasses MUST define platform and distribution (which may be None).\n    '
            var_0 = module_argument_spec_validator_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
