import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = None
            str_1 = "oa`\x0b[tcWu3)X=0g'b>)z"
            dict_0 = {str_0: str_0, str_1: str_0}
            list_0 = [dict_0, str_0]
            arg_0 = module_1.arg()
            variables_replacer_0 = module_0.VariablesReplacer(dict_0)
            arg_1 = variables_replacer_0.visit_arg(arg_0)
            class_def_0 = module_1.ClassDef()
            attribute_0 = module_1.Attribute(*list_0)
            snippet_0 = module_0.snippet(attribute_0)
            list_1 = snippet_0.get_body()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
