import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.return_from_generator as module_1

class Test_Return_from_generator_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            function_def_0 = module_0.FunctionDef()
            a_s_t_0 = module_0.AST()
            return_from_generator_transformer_0 = module_1.ReturnFromGeneratorTransformer(a_s_t_0)
            function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
