import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        tuple_0 = ()
        dict_0 = {}
        str_0 = 'Ha Gi?.+F~c@-'
        dict_1 = {str_0: dict_0}
        bool_0 = False
        set_0 = {tuple_0, str_0}
        validation_result_0 = module_0.ValidationResult(set_0)
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_1, bool_0, validation_result_0)
        var_0 = argument_spec_validator_0.validate(dict_1)
        validation_result_1 = module_0.ValidationResult(argument_spec_validator_0)

if __name__ == "__main__":
    unittest.main()
