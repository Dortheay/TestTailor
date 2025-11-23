import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = None
            str_1 = 'XO|4$ACHfwq+S?:;U'
            expr_0 = None
            list_0 = [expr_0, expr_0, expr_0]
            list_1 = [str_0]
            constant_0 = module_0.Constant(*list_1)
            str_2 = "6A)GFpA^;'`kyZ\r"
            str_3 = '5(GPiD?e73dsD-N)h>'
            str_4 = 'typing.AsyncIterable'
            int_0 = 1
            str_5 = 'Y8Q`Og'
            int_1 = 183
            str_6 = 'n69Wp.B^^b+/~JVY#SN'
            int_2 = 1
            dict_0 = {str_4: int_0, str_5: int_1, str_6: int_2, str_1: int_1}
            str_7 = ')2x}d,[\x0cemBiGC+xM@'
            dict_1 = {str_2: str_0, str_1: str_0, str_3: dict_0, str_7: str_4}
            class_def_0 = module_0.ClassDef(**dict_1)
            list_2 = [constant_0, class_def_0]
            bool_0 = True
            dict_2 = {}
            parser_0 = module_1.Parser(bool_0, dict_2, dict_2)
            parser_0.class_api(str_0, str_1, list_0, list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
