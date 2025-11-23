import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = 7
            generator_0 = module_0.roman_range(int_0)
            var_0 = list(generator_0)
            int_1 = 7
            int_2 = 1
            int_3 = -1
            generator_1 = module_0.roman_range(int_2, int_1, int_3)
            var_1 = list(generator_1)
            int_4 = 7
            int_5 = 1
            generator_2 = module_0.roman_range(int_5, int_4, int_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
