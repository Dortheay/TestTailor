import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        int_0 = 1922
        str_0 = 'gI'
        str_1 = module_0.shuffle(str_0)
        str_2 = module_0.roman_encode(int_0)
        str_3 = '#8)GXhw/g,y\x0bdb'
        str_4 = module_0.prettify(str_3)
        str_5 = 'ni_3[<c'
        str_6 = module_0.snake_case_to_camel(str_0, str_4)
        str_7 = module_0.strip_margin(str_1)
        str_8 = module_0.prettify(str_1)
        str_9 = '%JE'
        str_10 = module_0.strip_html(str_9)
        str_11 = module_0.prettify(str_2)
        str_12 = 'is_uuid'
        bool_0 = True
        str_13 = module_0.snake_case_to_camel(str_12, bool_0)
        str_14 = module_0.compress(str_5)
        str_15 = module_0.reverse(str_10)
        str_16 = module_0.slugify(str_1)
        int_1 = module_0.roman_decode(str_11)

if __name__ == "__main__":
    unittest.main()
