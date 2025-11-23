import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'Hn`$5Gv'
            bool_0 = module_1.is_public_family(str_0)
            str_1 = 'h4'
            assign_0 = module_0.Assign()
            str_2 = module_1.esc_underscore(str_0)
            int_0 = 1
            bool_1 = False
            int_1 = 1948
            dict_0 = {str_1: int_1, str_1: int_0}
            dict_1 = {str_1: str_1}
            parser_0 = module_1.Parser(int_0, bool_1, dict_0, dict_1, dict_1)
            parser_0.globals(str_1, assign_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
