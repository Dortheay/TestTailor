import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            int_0 = 5
            int_1 = 1
            int_2 = -1
            generator_0 = module_0.roman_range(int_1, int_0, int_2)
            var_0 = list(generator_0)
            int_3 = 4000
            generator_1 = module_0.roman_range(int_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
