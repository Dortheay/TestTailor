import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        dict_0 = {}
        arg_0 = module_0.arg(**dict_0)
        str_0 = "(:hd6R@'E**3PU#I#D0"
        dict_1 = {str_0: str_0, str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_1)
        arg_1 = variables_replacer_0.visit_arg(arg_0)

if __name__ == "__main__":
    unittest.main()
