import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        int_0 = 1922
        str_0 = '+AJ0:>!;sYX<I8Lc '
        str_1 = module_0.shuffle(str_0)
        str_2 = module_0.roman_encode(int_0)
        str_3 = '#8)GXhw/g,y\x0bdb'
        str_4 = module_0.prettify(str_3)
        str_5 = "1|'T%(}!K4"
        str_6 = 'n7/ia_3[<'
        str_7 = module_0.snake_case_to_camel(str_5, str_4)
        str_8 = module_0.strip_margin(str_1)
        str_9 = module_0.prettify(str_5)
        str_10 = '%JE'
        str_11 = module_0.strip_html(str_10)
        str_12 = module_0.prettify(str_5)
        str_13 = 'is_uuid'
        bool_0 = True
        str_14 = module_0.snake_case_to_camel(str_13, bool_0)
        str_15 = module_0.compress(str_6)
        str_16 = module_0.reverse(str_5)

if __name__ == "__main__":
    unittest.main()
