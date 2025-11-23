import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'ny'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            name_0 = module_1.Name(**dict_0)
            str_1 = None
            str_2 = 'J>WX[XVz0a'
            str_3 = 'VJVgp{,l*>:'
            dict_1 = {str_1: str_1, str_2: str_2, str_3: str_1}
            variables_replacer_0 = module_0.VariablesReplacer(dict_1)
            name_1 = variables_replacer_0.visit_Name(name_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
