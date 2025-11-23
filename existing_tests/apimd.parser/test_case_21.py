import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'S(2u%}!SELu'
            ann_assign_0 = module_0.AnnAssign()
            bool_0 = False
            str_1 = '0DK3'
            str_2 = 'Ux;\r0SDf/'
            str_3 = '*"7='
            dict_0 = {str_1: str_2, str_3: str_1}
            parser_0 = module_1.Parser(bool_0, dict_0)
            parser_0.globals(str_0, ann_assign_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
