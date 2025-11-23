import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        callable_0 = None
        snippet_0 = module_1.snippet(callable_0)
        str_0 = '"$T9,91,14t_XI'
        str_1 = 'tree'
        dict_0 = {str_0: str_0, str_0: callable_0, str_1: callable_0}
        function_def_0 = module_0.FunctionDef(**dict_0)
        str_2 = None
        attribute_0 = module_0.Attribute()
        dict_1 = {str_1: str_1, str_0: str_2}
        variables_replacer_0 = module_1.VariablesReplacer(dict_1)
        attribute_1 = variables_replacer_0.visit_Attribute(attribute_0)
        str_3 = '1LL^<4[Wb^er'
        a_s_t_0 = module_0.AST()
        module_1.extend_tree(a_s_t_0, dict_1)
        dict_2 = {str_2: str_0, str_0: str_1, str_2: str_0, str_3: str_3}
        variables_replacer_1 = module_1.VariablesReplacer(dict_2)
        name_0 = module_0.Name(**dict_0)

if __name__ == "__main__":
    unittest.main()
