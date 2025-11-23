import unittest
import timeout_decorator
import py_backwards.transformers.base as module_0
import typed_ast.ast3 as module_1
import typed_ast._ast3 as module_2

class Test_Base_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            a_s_t_0 = None
            base_node_transformer_0 = module_0.BaseNodeTransformer(a_s_t_0)
            base_import_rewrite_0 = module_0.BaseImportRewrite(a_s_t_0)
            list_0 = [a_s_t_0, base_import_rewrite_0]
            import_from_0 = module_2.ImportFrom(*list_0)
            var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
