import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 1323
            str_0 = module_0.secure_random_hex(int_0)
            int_1 = 3976
            int_2 = 697
            generator_0 = module_0.roman_range(int_1, int_2)
            generator_1 = module_0.roman_range(int_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
