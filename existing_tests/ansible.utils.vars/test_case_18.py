import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'key1'
            str_1 = 'key2'
            str_2 = 'value1'
            str_3 = 'value2'
            str_4 = {str_0: str_2, str_1: str_3}
            str_5 = 'key3'
            str_6 = 'override_value'
            str_7 = 'value3'
            str_8 = {str_1: str_6, str_5: str_7}
            bool_0 = False
            var_0 = module_0.combine_vars(str_4, str_8, bool_0)
            str_9 = 'subkey1'
            str_10 = 'subvalue1'
            str_11 = {str_9: str_10}
            str_12 = {str_0: str_2, str_1: str_11}
            str_13 = 'subkey2'
            str_14 = 'subvalue2'
            str_15 = {str_13: str_14}
            str_16 = {str_1: str_15, str_5: str_7}
            bool_1 = True
            var_1 = module_0.combine_vars(str_12, str_16, bool_1)
            str_17 = {str_0: str_2}
            str_18 = [str_4]
            bool_2 = False
            var_2 = module_0.combine_vars(str_17, str_18, bool_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
