import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        tuple_0 = ()
        dict_0 = {}
        str_0 = '%j`:wMR .8? 7zLE`'
        str_1 = 'Ha Gi?.+F~c@-'
        dict_1 = {str_1: dict_0}
        bool_0 = False
        set_0 = {tuple_0, str_1}
        validation_result_0 = module_0.ValidationResult(set_0)
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_1, bool_0, validation_result_0)
        validation_result_1 = module_0.ValidationResult(argument_spec_validator_0)
        list_0 = [str_0, tuple_0]
        str_2 = 'KZX\\JA[{N7{P7m)\\'
        dict_2 = {str_2: validation_result_1}
        var_0 = argument_spec_validator_0.validate(dict_2, *list_0)

if __name__ == "__main__":
    unittest.main()
