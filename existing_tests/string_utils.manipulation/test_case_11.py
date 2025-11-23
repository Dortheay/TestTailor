import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'FVu7v?(q]_2AwY#V'
            str_1 = module_0.roman_encode(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
