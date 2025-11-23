import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = None
        module_x_var_0 = None
        str_1 = 'ShRv:>F$ai\t\x0beD'
        str_2 = 'I '
        str_3 = '|s\\j:'
        str_4 = 'Sbb1'
        dict_0 = {str_3: str_2, str_2: str_4, str_1: str_1}
        set_0 = {str_2, str_3, str_1}
        dict_1 = {str_3: set_0}
        parser_0 = module_0.Parser(dict_0, dict_0, dict_1, dict_0)
        parser_0.load_docstring(str_0, module_x_var_0)

if __name__ == "__main__":
    unittest.main()
