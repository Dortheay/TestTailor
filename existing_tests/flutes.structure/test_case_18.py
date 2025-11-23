import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            var_0 = lambda x, y: x + y
            int_0 = 1
            int_1 = 2
            int_2 = 3
            int_3 = [int_0, int_1, int_2]
            int_4 = 4
            int_5 = 5
            int_6 = 6
            int_7 = [int_4, int_5, int_6]
            int_8 = [int_3, int_7]
            var_1 = module_0.map_structure_zip(var_0, int_8)
            var_2 = lambda x, y: x * y
            int_9 = [int_2, int_4]
            int_10 = [int_5, int_9]
            int_11 = [int_5, int_6]
            int_12 = 7
            int_13 = 8
            int_14 = [int_12, int_13]
            int_15 = [int_11, int_14]
            int_16 = [int_10, int_15]
            var_3 = module_0.map_structure_zip(var_2, int_16)
            var_4 = lambda x, y: x + y
            int_17 = (int_0, int_1, int_2)
            int_18 = (int_4, int_5, int_6)
            int_19 = [int_17, int_18]
            var_5 = module_0.map_structure_zip(var_4, int_19)
            var_6 = lambda x, y: x + y
            str_0 = 'a'
            str_1 = 'b'
            int_20 = {str_0: int_0, str_1: int_1}
            int_21 = {str_0: int_2, str_1: int_4}
            int_22 = [int_20, int_21]
            var_7 = module_0.map_structure_zip(var_6, int_22)
            var_8 = lambda x, y: x + y
            int_23 = [int_0, int_1]
            int_24 = [int_2, int_4]
            int_25 = {str_0: int_23, str_1: int_24}
            int_26 = [int_5, int_6]
            int_27 = [int_12, int_13]
            int_28 = {str_0: int_26, str_1: int_27}
            int_29 = [int_25, int_28]
            var_9 = module_0.map_structure_zip(var_8, int_29)
            var_10 = lambda x, y: x + y
            str_2 = 'a'
            str_3 = 'b'
            str_4 = {str_2, str_3}
            str_5 = 'd'
            str_6 = {str_2, str_5}
            str_7 = [str_4, str_6]
            var_11 = module_0.map_structure_zip(var_10, str_7)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
