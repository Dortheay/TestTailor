import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            function_def_0 = module_1.FunctionDef()
            list_0 = [function_def_0, function_def_0]
            str_0 = 'shlex_quote'
            dict_0 = {str_0: str_0}
            variables_replacer_0 = module_0.VariablesReplacer(dict_0)
            function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
            function_def_2 = variables_replacer_0.visit_FunctionDef(function_def_0)
            variables_replacer_1 = module_0.VariablesReplacer(dict_0)
            a_s_t_0 = module_1.AST(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
