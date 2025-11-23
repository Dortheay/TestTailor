import unittest
import timeout_decorator
import py_backwards.transformers.super_without_arguments as module_0
import typed_ast._ast3 as module_1

class Test_Super_without_arguments_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            call_0 = None
            a_s_t_0 = module_1.AST()
            super_without_arguments_transformer_0 = module_0.SuperWithoutArgumentsTransformer(a_s_t_0)
            call_1 = super_without_arguments_transformer_0.visit_Call(call_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
