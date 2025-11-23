import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '}\\IRY,xWBu*|<,dQ}2_p'
            dict_0 = {str_0: str_0, str_0: str_0}
            str_1 = 'ulekt>jjGR'
            list_0 = [str_1, dict_0, str_1]
            assign_0 = module_0.Assign(*list_0)
            int_0 = -499
            dict_1 = {str_0: int_0}
            str_2 = ']'
            set_0 = {str_0, str_2, str_0, str_2}
            str_3 = '?D1GUK5I?>"-SU'
            dict_2 = {str_0: set_0, str_2: set_0, str_3: set_0}
            dict_3 = {}
            parser_0 = module_1.Parser(dict_1, dict_2, dict_3, dict_3)
            parser_0.globals(str_1, assign_0)
            sequence_0 = module_2.Sequence(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
