import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1

class Test_Super_without_arguments_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'itertools'
        list_0 = [str_0, str_0, str_0]
        call_0 = module_0.Call(*list_0)
        a_s_t_0 = module_0.AST()
        super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
        call_1 = super_without_arguments_transformer_0.visit_Call(call_0)

if __name__ == "__main__":
    unittest.main()
