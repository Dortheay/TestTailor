import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_47(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_35(self):
        try:
            int_0 = 1922
            str_0 = 'gI'
            str_1 = module_0.shuffle(str_0)
            str_2 = module_0.roman_encode(int_0)
            str_3 = '#8)GXhw/g,y\x0bdb'
            str_4 = module_0.prettify(str_3)
            str_5 = "1|'T%(}!K4"
            str_6 = module_0.snake_case_to_camel(str_5, str_4)
            str_7 = module_0.strip_margin(str_1)
            str_8 = 'z ePbWP7<_QND!C@cJ_'
            var_0 = module_0.camel_case_to_snake(str_8)
            str_9 = module_0.prettify(str_5)
            str_10 = 'Invalid compression_level: it must be an "int" between 0 and 9'
            str_11 = module_0.prettify(str_10)
            str_12 = '%JE'
            bool_0 = True
            str_13 = module_0.strip_html(str_12, bool_0)
            str_14 = 'words_count'
            str_15 = module_0.prettify(str_14)
            str_16 = '_5b'
            str_17 = module_0.snake_case_to_camel(str_16)
            str_18 = None
            int_1 = -2805
            str_19 = module_0.compress(str_18, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
