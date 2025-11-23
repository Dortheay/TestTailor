import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = None
            generator_0 = module_0.roman_range(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
