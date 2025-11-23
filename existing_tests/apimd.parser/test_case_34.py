import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            bool_0 = False
            str_0 = '!/kU q(uvr<p_tD>'
            int_0 = 2022
            dict_0 = {str_0: int_0}
            str_1 = '4-'
            str_2 = ')N>lU-GT(e~5NX3t'
            str_3 = '@{vRpk!~u7CoHT[dZ'
            str_4 = 'd.p45? <'
            str_5 = '~.Yc`\rn?aA0,]0FQ'
            dict_1 = {str_1: str_2, str_3: str_4, str_3: str_5}
            str_6 = 'na'
            set_0 = set()
            str_7 = 'USr2NQ;UA\x0c0'
            dict_2 = {str_6: set_0, str_7: set_0}
            parser_0 = module_1.Parser(bool_0, dict_0, dict_1, dict_2, dict_1)
            str_8 = parser_0.compile()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
