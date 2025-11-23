import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        list_0 = []
        str_0 = 'x!8j9zH\x0cluGx\nCk\n'
        dict_0 = {str_0: list_0}
        class_def_0 = module_0.ClassDef(*list_0, **dict_0)
        str_1 = 'DDd]z0\\ZUy\r\nr^c|Ugw$'
        dict_1 = {str_1: str_1, str_1: str_1, str_1: str_1}
        variables_replacer_0 = module_1.VariablesReplacer(dict_1)
        class_def_1 = variables_replacer_0.visit_ClassDef(class_def_0)

if __name__ == "__main__":
    unittest.main()
