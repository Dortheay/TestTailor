import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            int_0 = 1922
            str_0 = 'gI'
            str_1 = module_0.shuffle(str_0)
            str_2 = module_0.roman_encode(int_0)
            str_3 = '#8)GXhw/g,y\x0bdb'
            str_4 = module_0.prettify(str_3)
            str_5 = 'bZ/~J9F<'
            bool_0 = True
            str_6 = module_0.snake_case_to_camel(str_5, bool_0)
            str_7 = module_0.strip_margin(str_4)
            float_0 = 1378.8
            var_0 = module_0.camel_case_to_snake(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
