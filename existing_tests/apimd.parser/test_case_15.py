import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        expr_0 = None
        str_0 = module_0.const_type(expr_0)
        str_1 = 'k6\x0c_3~v>_mE'
        expr_1 = module_1.expr()
        import_from_0 = module_1.ImportFrom()
        str_2 = 'dgCty})RuhC'
        str_3 = 'd|K6mB{tASj[0"(>Bze'
        str_4 = ''
        str_5 = '\x0b/B'
        str_6 = module_0.esc_underscore(str_4)
        str_7 = module_0.parent(str_5)
        str_8 = "mm;l{$+/'zYa*i={Lw5M"
        str_9 = "}mF[G0'1KR]/RV+"
        dict_0 = {}
        parser_0 = module_0.Parser(dict_0)
        str_10 = parser_0.resolve(str_8, expr_1, str_9)
        dict_1 = {str_2: str_3, str_3: str_4, str_5: str_2}
        parser_0.imports(str_1, import_from_0)
        str_11 = module_0.doctest(str_0)
        list_0 = [str_3, expr_1, dict_1, expr_1]
        dict_2 = {}
        str_12 = parser_0.compile()
        bool_0 = True
        str_13 = 'Wt(j\x0bq"K^[UU$'
        int_0 = 2175
        dict_3 = {str_13: int_0}
        dict_4 = {}
        parser_1 = module_0.Parser(bool_0, bool_0, dict_3, dict_4, dict_1)
        ann_assign_0 = module_1.AnnAssign(*list_0, **dict_2)
        str_14 = module_0.code(str_4)
        ann_assign_1 = module_1.AnnAssign(*list_0)
        expr_2 = module_1.expr(**dict_2)
        list_1 = [expr_2, str_11]
        subscript_0 = module_1.Subscript(*list_1)
        str_15 = '\r-9`AaM_/Q#7'
        str_16 = '\x0ct{i8r21S2'
        resolver_0 = module_0.Resolver(str_15, dict_0, str_16)
        a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
        str_17 = 'B]bWr=BJ::'
        parser_1.globals(str_17, ann_assign_1)
        str_18 = "gf'vtH3r)F2wcDCWc4"
        bool_1 = module_0.is_magic(str_18)

if __name__ == "__main__":
    unittest.main()
