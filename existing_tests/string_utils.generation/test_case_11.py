import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 3039
            str_0 = module_0.random_string(int_0)
            int_1 = 3
            str_1 = module_0.random_string(int_1)
            str_2 = module_0.uuid()
            str_3 = module_0.random_string(int_1)
            int_2 = 903
            int_3 = 573
            int_4 = -1604
            generator_0 = module_0.roman_range(int_2, int_3, int_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
