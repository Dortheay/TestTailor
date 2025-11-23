import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'PSRP RC{ %d'
            list_0 = []
            dict_0 = {str_0: list_0}
            var_0 = module_0.snake_dict_to_camel_dict(dict_0)
            set_0 = set()
            var_1 = module_0.dict_merge(list_0, set_0)
            float_0 = 2754.0
            int_0 = -1670
            var_2 = module_0.dict_merge(float_0, int_0)
            var_3 = module_0.camel_dict_to_snake_dict(dict_0)
            var_4 = module_0.dict_merge(set_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
