import unittest
import timeout_decorator
import py_backwards.transformers.base as module_0
import typed_ast.ast3 as module_1
import typed_ast._ast3 as module_2

class Test_Base_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            list_0 = []
            list_1 = [list_0, list_0, list_0]
            import_from_0 = module_2.ImportFrom(*list_1)
            a_s_t_0 = module_2.AST()
            base_import_rewrite_0 = module_0.BaseImportRewrite(a_s_t_0)
            var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
            a_s_t_1 = module_2.AST()
            var_1 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
            base_transformer_0 = module_0.BaseTransformer()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
