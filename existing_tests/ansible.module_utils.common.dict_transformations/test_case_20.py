import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'HttpEndpoint'
        str_1 = 'Tags'
        str_2 = 'NestedList'
        str_3 = 'EndpointUrl'
        str_4 = 'IsEnabled'
        str_5 = 'http://example.com'
        bool_0 = True
        var_0 = {str_3: str_5, str_4: bool_0}
        str_6 = 'Key'
        str_7 = 'Value'
        str_8 = 'Environment'
        str_9 = 'Production'
        str_10 = {str_6: str_8, str_7: str_9}
        str_11 = 'Owner'
        str_12 = 'TeamA'
        str_13 = {str_6: str_11, str_7: str_12}
        str_14 = [str_10, str_13]
        str_15 = 'InnerKey'
        str_16 = 'InnerValue'
        str_17 = {str_15: str_16}
        str_18 = 'DeepKey'
        str_19 = 'DeepValue'
        str_20 = {str_18: str_19}
        str_21 = [str_20]
        str_22 = [str_17, str_21]
        var_1 = {str_0: var_0, str_1: str_14, str_2: str_22}
        bool_1 = False
        str_23 = (str_1,)
        var_2 = module_0.camel_dict_to_snake_dict(var_1, bool_1, str_23)

if __name__ == "__main__":
    unittest.main()
