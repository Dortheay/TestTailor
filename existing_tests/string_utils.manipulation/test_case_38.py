import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            str_0 = 'gI'
            str_1 = module_0.shuffle(str_0)
            str_2 = "1|'T%(}!K4"
            str_3 = 'ni_3[<c'
            str_4 = module_0.strip_margin(str_1)
            str_5 = 'z ePbWP7<_QND!C@cJ_'
            var_0 = module_0.camel_case_to_snake(str_5)
            str_6 = module_0.prettify(str_2)
            str_7 = '%JE'
            str_8 = module_0.strip_html(str_7)
            str_9 = module_0.prettify(str_2)
            str_10 = 'is_uuid'
            bool_0 = False
            str_11 = module_0.snake_case_to_camel(str_10, bool_0)
            str_12 = module_0.compress(str_3)
            str_13 = module_0.reverse(str_2)
            int_0 = module_0.roman_decode(str_12)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
