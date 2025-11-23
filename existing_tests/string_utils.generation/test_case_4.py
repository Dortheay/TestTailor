import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 3
            str_0 = module_0.secure_random_hex(int_0)
            int_1 = -1296
            generator_0 = module_0.roman_range(int_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
