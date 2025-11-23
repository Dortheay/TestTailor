import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            int_0 = 1922
            str_0 = 'gI'
            str_1 = module_0.shuffle(str_0)
            str_2 = module_0.roman_encode(int_0)
            str_3 = '#8)GXhw/g,y\x0bdb'
            str_4 = module_0.prettify(str_3)
            str_5 = "1|'T%(}!K4"
            str_6 = 'ni_3[<c'
            str_7 = module_0.snake_case_to_camel(str_5, str_4)
            str_8 = module_0.strip_margin(str_1)
            str_9 = 'z ePbWP7<_QND!C@cJ_'
            var_0 = module_0.camel_case_to_snake(str_9)
            str_10 = module_0.prettify(str_5)
            str_11 = '%JE'
            str_12 = module_0.strip_html(str_11)
            str_13 = module_0.prettify(str_5)
            str_14 = '{P\nb'
            str_15 = module_0.snake_case_to_camel(str_14)
            int_1 = 903
            str_16 = module_0.compress(str_6, str_4, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
