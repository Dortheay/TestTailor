import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = '}\\IRY,xWBu*|<,dQ}2_p'
            dict_0 = {str_0: str_0, str_0: str_0}
            str_1 = '\\lekt>jj4GR'
            list_0 = [dict_0, str_1]
            assign_0 = module_0.Assign(*list_0)
            int_0 = -499
            dict_1 = {str_1: int_0, str_0: int_0}
            str_2 = module_1.parent(str_1)
            dict_2 = {}
            dict_3 = None
            parser_0 = module_1.Parser(int_0, dict_1, dict_3, dict_2, dict_2)
            parser_0.globals(str_1, assign_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
