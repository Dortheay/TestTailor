import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = 3
            str_0 = module_0.secure_random_hex(int_0)
            str_1 = module_0.random_string(int_0)
            int_1 = 2639
            str_2 = module_0.random_string(int_1)
            str_3 = module_0.secure_random_hex(int_1)
            int_2 = -1296
            int_3 = 2552
            generator_0 = module_0.roman_range(int_3, int_3, int_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
