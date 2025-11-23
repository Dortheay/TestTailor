import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = 'uYX!b70P+mbx\\s'
            str_1 = module_0.snake_case_to_camel(str_0)
            str_2 = module_0.strip_html(str_0)
            str_3 = 'NZeZ^'
            bool_0 = True
            str_4 = module_0.strip_html(str_3, bool_0)
            str_5 = 'cScR|g U52P\\qW|'
            int_0 = module_0.roman_decode(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
