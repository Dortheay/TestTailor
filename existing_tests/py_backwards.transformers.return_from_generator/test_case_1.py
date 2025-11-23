import unittest
import timeout_decorator
import py_backwards.transformers.return_from_generator as module_0
import typed_ast._ast3 as module_1

class Test_Return_from_generator_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        a_s_t_0 = module_1.AST()
        str_0 = 'F/54:^3jdu_87O'
        list_0 = [a_s_t_0, a_s_t_0, str_0, str_0, str_0]
        dict_0 = {str_0: a_s_t_0}
        function_def_0 = module_1.FunctionDef(*list_0, **dict_0)
        return_from_generator_transformer_0 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)
        function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)

if __name__ == "__main__":
    unittest.main()
