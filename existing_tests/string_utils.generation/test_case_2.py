import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = module_0.uuid()
            int_0 = 3999
            generator_0 = module_0.roman_range(int_0, int_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
