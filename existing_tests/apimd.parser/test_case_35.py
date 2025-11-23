import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            str_0 = "3F'qx .%"
            list_0 = [str_0]
            class_def_0 = module_0.ClassDef(*list_0)
            bool_0 = True
            int_0 = -3796
            str_1 = '?Mdi6K;_Wm_@R*>t'
            str_2 = '.72S='
            str_3 = "5G0<v\\'Vs'-g*"
            dict_0 = {str_1: str_2, str_3: str_1, str_3: str_2}
            parser_0 = module_1.Parser(bool_0, int_0, dict_0, dict_0, dict_0)
            parser_0.api(str_0, class_def_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
