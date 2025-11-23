import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            name_0 = module_0.Name()
            expr_0 = None
            str_0 = module_1.const_type(expr_0)
            expr_1 = module_0.expr()
            str_1 = module_1.const_type(expr_1)
            import_from_0 = module_0.ImportFrom()
            str_2 = 'Write file: '
            str_3 = '~4$I!&H'
            dict_0 = {}
            parser_0 = module_1.Parser(dict_0)
            str_4 = parser_0.resolve(str_2, expr_1, str_3)
            str_5 = '+ '
            function_def_0 = None
            str_6 = 'xJ/ES5^b, '
            dict_1 = {}
            parser_1 = module_1.Parser(dict_1, dict_0)
            parser_1.api(str_5, function_def_0, prefix=str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
