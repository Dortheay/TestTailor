import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        str_0 = 'h'
        assign_0 = module_1.Assign()
        int_0 = 23
        int_1 = 2914
        str_1 = 'y\ted\x0c,BJVb?Zm\x0byYXn'
        str_2 = module_0.doctest(str_1)
        str_3 = ' async '
        expr_0 = module_1.expr()
        str_4 = 'pT%~B\x0b]L<OG(8Vw^'
        str_5 = module_0.const_type(expr_0)
        list_0 = []
        import_0 = None
        list_1 = [assign_0, int_0, str_2, int_1]
        list_2 = [import_0, list_1]
        str_6 = None
        dict_0 = {str_4: str_2, str_4: str_6}
        parser_0 = module_0.Parser(dict_0, dict_0)
        parser_0.class_api(str_4, str_4, list_0, list_2)
        bool_0 = True
        str_7 = '-3-'
        str_8 = '+\r4-4oI\n=E'
        str_9 = 'qi|w\x0cLUxer7'
        str_10 = 'Constants'
        dict_1 = {str_7: str_8, str_1: str_0, str_9: str_10}
        parser_1 = module_0.Parser(bool_0, dict_1)
        str_11 = parser_1.compile()
        str_12 = 'Cl'
        bool_1 = module_0.is_public_family(str_12)
        str_13 = 'U(V3\\TjF{5;iqfvJ'
        module_x_var_0 = None
        parser_2 = module_0.Parser(bool_0, dict_1)
        parser_2.load_docstring(str_13, module_x_var_0)
        dict_2 = {str_0: int_1, str_0: int_1}
        dict_3 = {str_7: str_3}
        set_0 = set()
        str_14 = ']\tR'
        dict_4 = {str_0: set_0, str_14: set_0}
        parser_2.load_docstring(str_13, module_x_var_0)
        parser_3 = module_0.Parser(dict_2, dict_3, dict_4)
        str_15 = parser_3.compile()
        bool_2 = module_0.is_magic(str_14)

if __name__ == "__main__":
    unittest.main()
