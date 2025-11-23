import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'b__{[v'
            str_1 = module_1.esc_underscore(str_0)
            str_2 = module_1.doctest(str_0)
            int_0 = -718
            str_3 = None
            str_4 = None
            str_5 = 'YGkz\rt\x0bpXiie.^'
            str_6 = '1P-F;d<cYR_2'
            dict_0 = {str_3: str_2, str_4: str_0, str_2: str_5, str_3: str_6}
            set_0 = {str_1, str_6, str_5}
            dict_1 = {str_4: set_0, str_3: set_0}
            parser_0 = module_1.Parser(int_0, dict_0, dict_1)
            name_0 = module_0.Name()
            str_7 = '$dygK*srd'
            str_8 = 'typing.Awaitable'
            str_9 = '1MA/(x0~y'
            dict_2 = {str_8: str_9, str_8: str_7}
            str_10 = 'sI'
            resolver_0 = module_1.Resolver(str_7, dict_2, str_10)
            a_s_t_0 = resolver_0.visit_Name(name_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
