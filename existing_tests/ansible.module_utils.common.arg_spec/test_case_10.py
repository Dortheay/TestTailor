import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'name'
        str_1 = 'age'
        str_2 = 'type'
        str_3 = 'str'
        str_4 = {str_2: str_3}
        str_5 = 'aliases'
        str_6 = 'int'
        str_7 = 'years'
        str_8 = [str_7]
        str_9 = {str_2: str_6, str_5: str_8}
        str_10 = {str_0: str_4, str_1: str_9}
        str_11 = [str_0, str_1]
        str_12 = [str_11]
        str_13 = [str_0, str_1]
        str_14 = [str_13]
        str_15 = 'email'
        str_16 = [str_0, str_15]
        str_17 = [str_16]
        str_18 = 'status'
        str_19 = 'active'
        str_20 = [str_15]
        str_21 = [str_18, str_19, str_20]
        str_22 = [str_21]
        str_23 = 'parent'
        str_24 = 'child'
        str_25 = [str_24]
        str_26 = {str_23: str_25}
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(str_10, str_12, str_14, str_17, str_22, str_26)

if __name__ == "__main__":
    unittest.main()
