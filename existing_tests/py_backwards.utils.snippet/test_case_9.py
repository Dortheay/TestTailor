import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = None
            str_1 = "oa`\x0b[tcWu3)X=0g'b>)z"
            dict_0 = {str_0: str_0, str_1: str_0}
            arg_0 = module_1.arg()
            variables_replacer_0 = module_0.VariablesReplacer(dict_0)
            arg_1 = None
            arg_2 = variables_replacer_0.visit_arg(arg_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
