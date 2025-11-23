import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_44(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
        try:
            int_0 = -992
            str_0 = 'gI'
            str_1 = module_0.shuffle(str_0)
            str_2 = module_0.roman_encode(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
