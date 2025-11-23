import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            int_0 = 2147
            str_0 = module_0.roman_encode(int_0)
            str_1 = 'C'
            str_2 = module_0.roman_encode(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
