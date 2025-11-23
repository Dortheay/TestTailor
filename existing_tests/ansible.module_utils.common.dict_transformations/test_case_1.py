import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            float_0 = -2100.0516
            dict_0 = {bool_0: bool_0, bool_0: bool_0, float_0: float_0}
            list_0 = []
            var_0 = module_0.camel_dict_to_snake_dict(dict_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
