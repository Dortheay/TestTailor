import unittest
import timeout_decorator
import py_backwards.transformers.base as module_0
import typed_ast.ast3 as module_1
import typed_ast._ast3 as module_2

class Test_Base_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'import old_module'
            var_0 = module_1.parse(str_0)
            int_0 = 0
            var_1 = var_0.body[int_0]
            base_import_rewrite_0 = module_0.BaseImportRewrite(var_0)
            var_2 = base_import_rewrite_0.visit_Import(var_1)
            var_3 = var_2.body[int_0]
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
