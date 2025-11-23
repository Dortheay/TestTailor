import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = ''
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            var_0 = module_0.dict_merge(dict_0, dict_0)
            bool_0 = True
            set_0 = {str_0}
            int_0 = -1393
            list_0 = [var_0, int_0]
            list_1 = [bool_0, list_0, str_0]
            var_1 = module_0.camel_dict_to_snake_dict(set_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
