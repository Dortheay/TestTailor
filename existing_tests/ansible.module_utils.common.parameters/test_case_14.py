import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'default_release'
            str_1 = 'f\t>7D$9+i\t'
            str_2 = '{\rO03oycm`m%]6'
            dict_0 = {str_0: str_0, str_1: str_0, str_2: str_0, str_2: str_1}
            str_3 = 'LPAR Info'
            var_0 = module_0.remove_values(dict_0, str_3)
            int_0 = -1279
            list_0 = [dict_0, str_2, int_0, str_1]
            var_1 = module_0.env_fallback(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
