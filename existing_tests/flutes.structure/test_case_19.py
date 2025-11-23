import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            var_0 = lambda x, y: x + y
            int_0 = 1
            int_1 = -126
            int_2 = [int_0, int_1, int_1]
            int_3 = 4
            int_4 = 5
            int_5 = 6
            int_6 = [int_3, int_4, int_5]
            int_7 = [int_2, int_6]
            var_1 = module_0.map_structure_zip(var_0, int_7)
            var_2 = lambda x, y: x * y
            int_8 = [int_0, int_4]
            int_9 = [int_8, int_1]
            int_10 = [int_4, int_5]
            int_11 = 7
            int_12 = [int_11, int_0]
            int_13 = [int_10, int_12]
            int_14 = [int_9, int_13]
            var_3 = module_0.map_structure_zip(var_2, int_14)
            int_15 = (int_0, int_14, int_1)
            int_16 = [int_15, int_7]
            var_4 = module_0.map_structure_zip(int_10, int_16)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
