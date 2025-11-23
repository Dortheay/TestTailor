import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = False
            bool_0 = True
            int_1 = 701
            generator_0 = module_0.roman_range(int_1)
            str_0 = module_0.uuid(bool_0)
            str_1 = module_0.secure_random_hex(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
