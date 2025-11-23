import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'FQzEZ4=tdFm|}'
            str_1 = 'AoqU'
            str_2 = 'nX0;'
            str_3 = 'NmTFwObHJ74yV\\|'
            set_0 = {str_3}
            dict_0 = {str_0: set_0}
            dict_1 = {str_1: str_0, str_2: str_2, str_1: str_2, str_3: dict_0}
            class_def_0 = module_0.ClassDef(**dict_1)
            int_0 = -788
            parser_0 = module_1.Parser(int_0)
            parser_0.api(str_0, class_def_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
