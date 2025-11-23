import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'CamelCaseKey'
        str_1 = 'NestedDict'
        str_2 = 'IgnoreMe'
        str_3 = 'InnerKey'
        str_4 = 'AnotherInnerKey'
        str_5 = 'DeepKey'
        str_6 = {str_5: str_0}
        str_7 = {str_3: str_0, str_4: str_6}
        str_8 = 'value1'
        str_9 = 'value2'
        str_10 = {str_3: str_9}
        str_11 = [str_4, str_10]
        str_12 = 'PreserveKey'
        str_13 = {str_12: str_7}
        str_14 = {str_0: str_10, str_1: str_7, str_8: str_11, str_2: str_13}
        str_15 = (str_2,)
        var_0 = module_0.camel_dict_to_snake_dict(str_14, str_15)

if __name__ == "__main__":
    unittest.main()
