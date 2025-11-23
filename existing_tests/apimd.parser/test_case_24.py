import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            constant_0 = module_0.Constant()
            str_0 = ''
            str_1 = '+ ['
            dict_0 = {str_0: str_1}
            str_2 = '2\x0buy3M\nM9\x0clHkI!h"^'
            bool_0 = module_1.is_public_family(str_1)
            str_3 = module_1.esc_underscore(str_0)
            str_4 = '?tQ'
            bool_1 = False
            parser_0 = module_1.Parser(bool_1, bool_1, dict_0)
            dict_1 = {str_1: constant_0, str_4: str_0}
            arguments_0 = module_0.arguments(**dict_1)
            expr_0 = module_0.expr()
            bool_2 = None
            bool_3 = False
            parser_1 = module_1.Parser(dict_0, dict_0, dict_0)
            parser_1.func_api(str_0, str_2, arguments_0, expr_0, has_self=bool_2, cls_method=bool_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
