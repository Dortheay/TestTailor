import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'key1'
        str_1 = 'key2'
        str_2 = 'value1'
        str_3 = 'value2'
        str_4 = {str_0: str_2, str_1: str_3}
        str_5 = 'key3'
        str_6 = 'value3'
        str_7 = {str_1: str_5, str_5: str_6}
        var_0 = module_0.dict_merge(str_4, str_7)
        str_8 = 'subkey1'
        str_9 = {str_8: str_2}
        str_10 = {str_0: str_9, str_1: str_3}
        str_11 = 'subkey2'
        str_12 = {str_11: str_3}
        str_13 = {str_0: str_12, str_5: str_6}
        var_1 = module_0.dict_merge(str_10, str_13)
        str_14 = {str_8: str_2}
        str_15 = {str_0: str_14}
        str_16 = 'new_value'
        str_17 = {str_0: str_16}
        var_2 = module_0.dict_merge(str_15, str_17)
        str_18 = {str_0: str_2}
        str_19 = 'not_a_dict'
        var_3 = module_0.dict_merge(str_18, str_19)
        var_4 = {}
        var_5 = {}
        var_6 = module_0.dict_merge(var_4, var_5)

if __name__ == "__main__":
    unittest.main()
