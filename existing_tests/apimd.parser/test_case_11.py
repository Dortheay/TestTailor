import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        expr_0 = module_1.expr()
        import_from_0 = module_1.ImportFrom()
        str_0 = 'd|K6mB{tASj[0"(>Bze'
        str_1 = ']'
        str_2 = '\x0b/\r'
        str_3 = module_0.esc_underscore(str_1)
        str_4 = module_0.parent(str_2)
        str_5 = 'Write file: '
        str_6 = "}mF[G0'1KR]/RV+"
        dict_0 = {}
        parser_0 = module_0.Parser(dict_0)
        str_7 = parser_0.resolve(str_5, expr_0, str_6)
        dict_1 = {str_7: str_2, str_0: str_1, str_2: str_7}
        parser_0.imports(str_3, import_from_0)
        str_8 = module_0.doctest(str_5)
        str_9 = 'Cl'
        list_0 = [str_0, expr_0, dict_1, expr_0]
        dict_2 = {}
        str_10 = parser_0.compile()
        ann_assign_0 = module_1.AnnAssign(*list_0, **dict_2)
        parser_0.globals(str_9, ann_assign_0)

if __name__ == "__main__":
    unittest.main()
