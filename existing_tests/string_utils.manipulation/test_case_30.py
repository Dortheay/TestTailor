import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            roman_numbers_0 = module_0.__RomanNumbers()
            str_0 = '`Q1w_r(k[q4@2T\x0c\x0c*T<'
            bool_0 = True
            str_1 = module_0.strip_html(str_0, bool_0)
            str_2 = None
            str_3 = module_0.snake_case_to_camel(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
