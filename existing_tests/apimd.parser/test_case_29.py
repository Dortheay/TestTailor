import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            bool_0 = True
            dict_0 = None
            dict_1 = None
            str_0 = 'QE6:?2"m[e)T8)>'
            str_1 = ',s`j\r'
            dict_2 = {str_1: str_0, str_1: dict_0, str_0: bool_0}
            constant_0 = module_0.Constant(**dict_2)
            str_2 = '6f'
            resolver_0 = module_1.Resolver(str_2, dict_1)
            str_3 = 'Xq'
            list_0 = [dict_2]
            subscript_0 = module_0.Subscript(*list_0)
            list_1 = [subscript_0]
            import_from_0 = module_0.ImportFrom(*list_1, **dict_2)
            parser_0 = module_1.Parser(dict_0, dict_1)
            parser_0.imports(str_3, import_from_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
