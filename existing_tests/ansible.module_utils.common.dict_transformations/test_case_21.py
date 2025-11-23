import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = 'HTTPEndpoint'
        str_1 = 'SomeNestedDict'
        str_2 = 'Tags'
        str_3 = 'value1'
        str_4 = 'InnerKey'
        str_5 = 'DeepList'
        str_6 = 'value2'
        str_7 = 'ListCamelKey'
        str_8 = 'value3'
        str_9 = {str_7: str_8}
        str_10 = 'value4'
        str_11 = [str_9, str_10]
        str_12 = {str_4: str_6, str_5: str_11}
        str_13 = 'Key'
        str_14 = 'Value'
        str_15 = 'TagKey'
        str_16 = 'TagValue'
        str_17 = {str_13: str_15, str_14: str_16}
        str_18 = [str_17]
        str_19 = {str_0: str_3, str_1: str_12, str_2: str_18}
        bool_0 = True
        str_20 = (str_2,)
        var_0 = module_0.camel_dict_to_snake_dict(str_19, bool_0, str_20)

if __name__ == "__main__":
    unittest.main()
