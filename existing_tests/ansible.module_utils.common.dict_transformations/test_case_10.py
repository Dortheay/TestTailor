import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'a'
            int_0 = 1
            str_1 = 'c'
            str_2 = 'd'
            int_1 = 2
            int_2 = 3
            int_3 = {str_0: int_0, str_1: int_1}
            int_4 = {str_0: int_0, str_2: int_2}
            var_0 = module_0.recursive_diff(int_3, int_4)
            int_5 = {str_0: int_0, str_0: int_1}
            int_6 = {str_0: int_0, str_1: int_2}
            var_1 = module_0.recursive_diff(int_5, int_6)
            str_3 = 'nested'
            int_7 = {str_3: int_0}
            int_8 = {str_0: int_7, str_3: int_1}
            int_9 = {str_3: int_1}
            int_10 = {str_0: int_9, str_0: int_1}
            var_2 = module_0.recursive_diff(int_8, int_10)
            int_11 = {str_0: int_0}
            int_12 = {str_0: int_0, str_2: int_1}
            var_3 = module_0.recursive_diff(int_11, int_12)
            str_4 = 'a'
            int_13 = 1
            int_14 = {str_4: int_13}
            str_5 = 'invalid'
            str_6 = 'input'
            str_7 = [str_5, str_6]
            var_4 = module_0.recursive_diff(int_14, str_7)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
