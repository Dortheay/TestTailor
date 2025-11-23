import unittest
import timeout_decorator
import py_backwards.transformers.return_from_generator as module_0
import typed_ast._ast3 as module_1

class Test_Return_from_generator_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b''
        str_0 = '+tQU\tGl\\'
        dict_0 = {str_0: str_0}
        a_s_t_0 = module_1.AST()
        return_from_generator_transformer_0 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)
        a_s_t_1 = module_1.AST()
        a_s_t_2 = module_1.AST(**dict_0)
        list_0 = [bytes_0, bytes_0, bytes_0]
        function_def_0 = module_1.FunctionDef(*list_0)
        return_from_generator_transformer_1 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)
        return_from_generator_transformer_2 = module_0.ReturnFromGeneratorTransformer(a_s_t_1)
        return_from_generator_transformer_3 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)
        function_def_1 = return_from_generator_transformer_0.visit_FunctionDef(function_def_0)
        function_def_2 = return_from_generator_transformer_3.visit_FunctionDef(function_def_0)
        function_def_3 = return_from_generator_transformer_3.visit_FunctionDef(function_def_2)
        function_def_4 = return_from_generator_transformer_2.visit_FunctionDef(function_def_2)
        return_from_generator_transformer_4 = module_0.ReturnFromGeneratorTransformer(a_s_t_2)
        return_from_generator_transformer_5 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)
        function_def_5 = return_from_generator_transformer_4.visit_FunctionDef(function_def_0)
        return_from_generator_transformer_6 = module_0.ReturnFromGeneratorTransformer(a_s_t_1)
        return_from_generator_transformer_7 = module_0.ReturnFromGeneratorTransformer(a_s_t_2)
        function_def_6 = return_from_generator_transformer_7.visit_FunctionDef(function_def_1)
        return_from_generator_transformer_8 = module_0.ReturnFromGeneratorTransformer(a_s_t_2)
        return_from_generator_transformer_9 = module_0.ReturnFromGeneratorTransformer(a_s_t_2)
        function_def_7 = return_from_generator_transformer_4.visit_FunctionDef(function_def_3)
        return_from_generator_transformer_10 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
