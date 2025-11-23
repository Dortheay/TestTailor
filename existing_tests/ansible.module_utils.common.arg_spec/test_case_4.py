import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            tuple_0 = ()
            dict_0 = {tuple_0: tuple_0}
            dict_1 = {}
            str_0 = '%j`:wMR .8? 7zLE`'
            str_1 = 'Ha Gi?.+F~c@-'
            dict_2 = {str_1: dict_0}
            float_0 = -1816.63
            bool_0 = False
            set_0 = {tuple_0, str_1}
            validation_result_0 = module_0.ValidationResult(set_0)
            argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_2, bool_0, validation_result_0)
            var_0 = argument_spec_validator_0.validate(dict_2)
            validation_result_1 = module_0.ValidationResult(argument_spec_validator_0)
            list_0 = [dict_1, str_0]
            module_argument_spec_validator_0 = module_0.ModuleArgumentSpecValidator(*list_0)
            var_1 = module_argument_spec_validator_0.validate(dict_0)
            int_0 = 686
            str_2 = 'R1we(ID;#Lo^,aZ1['
            argument_spec_validator_1 = module_0.ArgumentSpecValidator(float_0, int_0, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
