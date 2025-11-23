import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'PSRP RC{ %d'
        list_0 = []
        dict_0 = {str_0: list_0}
        var_0 = module_0.snake_dict_to_camel_dict(dict_0)
        var_1 = module_0.camel_dict_to_snake_dict(dict_0)
        list_1 = [dict_0, dict_0]
        str_1 = 'untagged'
        var_2 = module_0.snake_dict_to_camel_dict(list_1, str_1)

if __name__ == "__main__":
    unittest.main()
