import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = -948
            str_0 = 'i:0w[$"/$!x'
            str_1 = 'E-Bg\t1'
            str_2 = None
            str_3 = 'Seth Michael Larson'
            int_1 = None
            str_4 = 'wdeEw.'
            var_0 = module_0.container_to_text(int_1, str_4)
            dict_0 = {str_0: str_0, str_1: int_0, str_2: str_2, str_3: int_0}
            var_1 = module_0.container_to_bytes(dict_0)
            set_0 = {str_2}
            bool_0 = True
            bool_1 = False
            var_2 = module_0.container_to_text(bool_0, bool_1)
            bool_2 = False
            var_3 = module_0.container_to_text(set_0, bool_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
