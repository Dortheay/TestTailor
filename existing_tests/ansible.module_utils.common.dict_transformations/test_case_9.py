import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'a'
            str_1 = 'b'
            int_0 = 1
            str_2 = 'c'
            str_3 = 'd'
            int_1 = 2
            int_2 = 3
            int_3 = {str_2: int_1, str_3: int_2}
            int_4 = {str_0: int_0, str_1: int_3}
            int_5 = {str_2: int_1, str_3: int_2}
            int_6 = {str_0: int_0, str_1: int_5}
            var_0 = module_0.recursive_diff(int_4, int_6)
            int_7 = {str_0: int_0, str_1: int_1}
            int_8 = {str_0: int_0, str_1: int_1}
            int_9 = {str_0: int_0, str_2: int_2}
            var_1 = module_0.recursive_diff(int_8, int_9)
            str_4 = 'nested'
            int_10 = {str_4: int_0}
            int_11 = {str_0: int_10, str_1: int_1}
            int_12 = {str_4: int_1}
            int_13 = {str_0: int_12, str_1: int_1}
            var_2 = module_0.recursive_diff(int_11, int_13)
            int_14 = {str_0: int_0}
            int_15 = {str_0: int_0, str_1: int_1}
            var_3 = module_0.recursive_diff(int_14, int_15)
            str_5 = 'input'
            str_6 = [str_1, str_5]
            var_4 = module_0.recursive_diff(int_7, str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
