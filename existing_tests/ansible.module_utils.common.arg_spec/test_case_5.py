import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'name'
            str_1 = 'age'
            str_2 = 'vip'
            str_3 = 'type'
            str_4 = 'required'
            str_5 = 'str'
            bool_0 = True
            var_0 = {str_3: str_5, str_4: bool_0}
            str_6 = 'int'
            str_7 = {str_3: str_6}
            str_8 = 'default'
            str_9 = 'aliases'
            str_10 = 'bool'
            bool_1 = False
            str_11 = 'vip_user'
            str_12 = [str_11]
            var_1 = {str_3: str_10, str_8: bool_1, str_9: str_12}
            var_2 = {str_0: var_0, str_1: str_7, str_2: var_1}
            str_13 = 'Alice'
            int_0 = 30
            var_3 = {str_0: str_13, str_1: int_0, str_11: bool_0}
            str_14 = [str_1, str_11]
            str_15 = [str_14]
            argument_spec_validator_0 = module_0.ArgumentSpecValidator(var_2, str_15)
            var_4 = argument_spec_validator_0.validate(var_3)
            var_5 = var_4.validated_parameters
            var_6 = {str_0: str_13, str_1: int_0, str_2: bool_0}
            var_7 = argument_spec_validator_0.validate(var_6)
            var_8 = var_7.error_messages
            var_9 = len(var_8)
            var_10 = var_7.errors[bool_1]
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
