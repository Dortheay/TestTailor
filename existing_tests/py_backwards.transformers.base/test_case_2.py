import unittest
import timeout_decorator
import py_backwards.transformers.base as module_0
import typed_ast.ast3 as module_1
import typed_ast._ast3 as module_2

class Test_Base_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'N{S{.T\t9aK\n,;BS/'
            str_1 = 'Z'
            dict_0 = {str_0: str_0, str_1: str_1, str_0: str_1, str_0: str_0}
            list_0 = [str_0, str_1]
            list_1 = [str_0, list_0, dict_0]
            import_from_0 = module_2.ImportFrom(*list_1)
            a_s_t_0 = module_2.AST()
            base_import_rewrite_0 = module_0.BaseImportRewrite(a_s_t_0)
            var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
