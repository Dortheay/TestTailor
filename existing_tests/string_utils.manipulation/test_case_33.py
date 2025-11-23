import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            str_0 = ';R'
            bool_0 = module_0.booleanize(str_0)
            str_1 = module_0.shuffle(str_0)
            str_2 = 'strip_html'
            str_3 = module_0.strip_margin(str_2)
            str_4 = module_0.prettify(str_3)
            int_0 = module_0.roman_decode(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
