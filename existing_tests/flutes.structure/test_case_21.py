import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
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
            int_9 = [int_0, int_1]
            int_10 = [int_2, int_4]
            int_11 = [int_9, int_10]
            int_12 = [int_5, int_6]
            int_13 = 7
            int_14 = 8
            int_15 = [int_13, int_14]
            int_16 = [int_12, int_15]
            int_17 = [int_11, int_16]
            var_2 = module_0.map_structure_zip(var_0, int_17)
            str_0 = 'a'
            str_1 = 'b'
            int_18 = {str_0: int_0, str_1: int_1}
            int_19 = 10
            int_20 = 20
            int_21 = {str_0: int_19, str_1: int_20}
            int_22 = [int_18, int_21]
            var_3 = module_0.map_structure_zip(var_0, int_22)
            int_23 = (int_0, int_1, int_2)
            int_24 = (int_4, int_5, int_6)
            int_25 = [int_23, int_24]
            var_4 = module_0.map_structure_zip(var_0, int_25)
            var_5 = module_0.map_structure_zip(var_0, int_25)
            int_26 = [int_0, int_1]
            int_27 = (int_2, int_4)
            int_28 = {str_0: int_26, str_1: int_27}
            int_29 = [int_5, int_6]
            int_30 = (int_13, int_14)
            int_31 = {str_0: int_29, str_1: int_30}
            int_32 = [int_28, int_31]
            var_6 = module_0.map_structure_zip(var_0, int_32)
            str_2 = 'custom_key'
            int_33 = 100
            int_34 = {str_2: int_33}
            var_7 = module_0.no_map_instance(int_34)
            int_35 = 200
            int_36 = {str_2: int_35}
            var_8 = module_0.no_map_instance(int_36)
            var_9 = [var_7, var_8]
            var_10 = module_0.map_structure_zip(var_0, var_9)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
