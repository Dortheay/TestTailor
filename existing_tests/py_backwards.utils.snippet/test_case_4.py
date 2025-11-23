import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = "mh0:/'KhU"
            str_1 = '{[>`ZO"@ '
            dict_0 = {str_0: str_0, str_1: str_1}
            variables_replacer_0 = module_0.VariablesReplacer(dict_0)
            keyword_0 = module_1.keyword()
            variables_replacer_1 = module_0.VariablesReplacer(dict_0)
            keyword_1 = variables_replacer_1.visit_keyword(keyword_0)
            keyword_2 = variables_replacer_0.visit_keyword(keyword_1)
            arg_0 = None
            dict_1 = {}
            variables_replacer_2 = module_0.VariablesReplacer(dict_1)
            bool_0 = False
            snippet_0 = module_0.snippet(bool_0)
            snippet_1 = module_0.snippet(snippet_0)
            arg_1 = variables_replacer_2.visit_arg(arg_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
