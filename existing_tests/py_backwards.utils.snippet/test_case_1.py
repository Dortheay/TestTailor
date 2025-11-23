import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            except_handler_0 = None
            str_0 = 'HU&#\x0cg4NB'
            str_1 = 'Cookie'
            dict_0 = {str_0: str_0, str_1: str_0, str_0: str_1, str_1: str_0}
            variables_replacer_0 = module_0.VariablesReplacer(dict_0)
            except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
