import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = 'h'
            assign_0 = module_0.Assign()
            int_0 = 23
            int_1 = 3
            str_1 = 'y\ted\x0c,BJVb?Zm\x0byYXn'
            str_2 = module_1.doctest(str_1)
            bool_0 = module_1.is_public_family(str_1)
            str_3 = ' async '
            expr_0 = module_0.expr()
            str_4 = 'pT%~B\x0b]L<OG(8Vw^'
            bool_1 = True
            bool_2 = True
            str_5 = '-3-'
            str_6 = 'N_o\r7k%H,G['
            dict_0 = {str_5: int_1, str_6: int_0, str_0: int_0, str_6: int_1}
            str_7 = '+\r4-4oI\n=E'
            str_8 = 'qi|w\x0cLUxer7'
            str_9 = 'Constants'
            dict_1 = {str_5: str_7, str_1: str_0, str_8: str_9}
            parser_0 = module_1.Parser(bool_1, bool_2, dict_0, dict_1)
            str_10 = parser_0.resolve(str_3, expr_0, str_4)
            dict_2 = {}
            list_0 = [int_0]
            name_0 = module_0.Name(*list_0)
            str_11 = 'k6'
            resolver_0 = module_1.Resolver(str_6, dict_2, str_11)
            a_s_t_0 = resolver_0.visit_Name(name_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
