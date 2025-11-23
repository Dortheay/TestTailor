import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'h4'
            assign_0 = module_0.Assign()
            int_0 = 1
            bool_0 = False
            int_1 = 1948
            dict_0 = {str_0: int_1, str_0: int_0}
            dict_1 = {str_0: str_0}
            parser_0 = module_1.Parser(int_0, bool_0, dict_0, dict_1, dict_1)
            parser_0.globals(str_0, assign_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
