import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
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
            int_9 = [int_0, int_1]
            int_10 = [int_2, int_4]
            int_11 = [int_9, int_10]
            int_12 = [int_5, int_6]
            int_13 = 7
            int_14 = [int_13, int_0]
            int_15 = [int_12, int_14]
            int_16 = [int_11, int_15]
            var_3 = module_0.map_structure_zip(var_2, int_16)
            var_4 = lambda x, y: x + y
            int_17 = (int_0, int_1, int_2)
            int_18 = (int_4, int_5, int_6)
            int_19 = [int_17, int_18]
            var_5 = module_0.map_structure_zip(var_4, int_19)
            str_0 = 'a'
            str_1 = 'b'
            int_20 = {str_0: int_0, str_1: int_1}
            int_21 = {str_0: int_2, str_1: int_4}
            int_22 = [int_20, int_21]
            var_6 = module_0.map_structure_zip(int_12, int_22)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
