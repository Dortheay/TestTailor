import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            str_0 = '\tQ'
            bool_0 = True
            int_0 = -4777
            str_1 = 'RoYP;0gj4^\t8BW;(U:9.'
            str_2 = 'TPb0cxUg)nd'
            str_3 = None
            str_4 = ''
            dict_0 = {str_0: str_1, str_1: str_0, str_2: str_0, str_3: str_4}
            str_5 = None
            list_0 = [str_0]
            arguments_0 = module_0.arguments(*list_0)
            resolver_0 = module_1.Resolver(str_3, dict_0)
            bool_1 = True
            bool_2 = True
            int_1 = 2386
            int_2 = 1
            dict_1 = {str_3: int_2, str_0: int_0}
            parser_0 = module_1.Parser(bool_2, int_1, dict_1, dict_0, dict_0, dict_0)
            parser_0.func_api(str_5, str_0, arguments_0, resolver_0, has_self=bool_0, cls_method=bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
