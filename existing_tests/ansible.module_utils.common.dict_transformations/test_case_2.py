import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            set_0 = set()
            float_0 = -882.6
            str_0 = 'PSRP RC: %d'
            list_0 = []
            var_0 = module_0.snake_dict_to_camel_dict(list_0, float_0)
            var_1 = module_0.recursive_diff(str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
