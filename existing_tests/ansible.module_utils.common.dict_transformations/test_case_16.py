import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'PSRP RC{ %d'
        list_0 = [str_0]
        dict_0 = {str_0: list_0}
        var_0 = module_0.snake_dict_to_camel_dict(dict_0)
        set_0 = set()
        var_1 = module_0.dict_merge(list_0, set_0)
        var_2 = module_0.camel_dict_to_snake_dict(dict_0)
        str_1 = 'untagged'
        var_3 = module_0.snake_dict_to_camel_dict(list_0, str_1)
        var_4 = module_0.recursive_diff(dict_0, dict_0)

if __name__ == "__main__":
    unittest.main()
