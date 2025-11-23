import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '\x0b|'
            str_1 = module_0.shuffle(str_0)
            str_2 = 'P1KC%f\tSjEy87#}b4'
            str_3 = module_0.strip_margin(str_2)
            str_4 = module_0.prettify(str_2)
            str_5 = "]\r?cjZC'`'V"
            int_0 = module_0.roman_decode(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
