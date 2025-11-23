import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            assign_0 = module_0.Assign()
            int_0 = 3
            str_0 = 'y\ted\x0c,BJVb?Zm\x0byYXn'
            str_1 = module_1.doctest(str_0)
            bool_0 = module_1.is_public_family(str_0)
            expr_0 = module_0.expr()
            bool_1 = True
            str_2 = '4'
            dict_0 = {str_2: int_0}
            dict_1 = {str_2: str_1}
            parser_0 = module_1.Parser(bool_1, int_0, dict_0, dict_1, dict_1, dict_1)
            str_3 = parser_0.compile()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
