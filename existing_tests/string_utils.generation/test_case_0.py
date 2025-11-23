import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = 855
        str_0 = module_0.random_string(int_0)

if __name__ == "__main__":
    unittest.main()
