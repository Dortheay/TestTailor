import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            int_0 = 1922
            str_0 = 'gI'
            str_1 = module_0.shuffle(str_0)
            str_2 = module_0.roman_encode(int_0)
            str_3 = module_0.prettify(str_1)
            str_4 = "1|'T%(}!K4"
            str_5 = 'ni_3[<c'
            str_6 = module_0.snake_case_to_camel(str_4, str_3)
            str_7 = module_0.strip_margin(str_1)
            str_8 = 'z ePbWP7<_QND!C@cJ_'
            var_0 = module_0.camel_case_to_snake(str_8)
            str_9 = module_0.prettify(str_4)
            str_10 = '%JE'
            str_11 = module_0.strip_html(str_10)
            str_12 = module_0.prettify(str_4)
            str_13 = 'is_uuid'
            bool_0 = False
            str_14 = module_0.snake_case_to_camel(str_13, bool_0)
            str_15 = module_0.compress(str_5)
            str_16 = module_0.compress(str_11)
            str_17 = "-'=Ih3zEf,Xes26#hb("
            str_18 = module_0.reverse(str_17)
            str_19 = '\n'
            int_1 = module_0.roman_decode(str_19)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
