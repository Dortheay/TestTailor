import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = 2153
        str_0 = module_0.roman_encode(int_0)
        str_1 = 'V*'
        str_2 = module_0.compress(str_1)

if __name__ == "__main__":
    unittest.main()
