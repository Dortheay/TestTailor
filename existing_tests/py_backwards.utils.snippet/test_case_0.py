import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '*7J)]n-}7M\x0cdG'
            dict_0 = {str_0: str_0}
            variables_replacer_0 = module_0.VariablesReplacer(dict_0)
            arg_0 = None
            str_1 = "H'WR"
            str_2 = 'shlex_quote'
            dict_1 = {str_1: str_1, str_2: str_2, str_2: str_2, str_2: str_2}
            variables_replacer_1 = module_0.VariablesReplacer(dict_1)
            list_0 = [str_2, str_0]
            name_0 = module_1.Name(*list_0)
            name_1 = variables_replacer_1.visit_Name(name_0)
            arg_1 = variables_replacer_1.visit_arg(arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
