import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            dict_0 = {}
            except_handler_0 = module_1.ExceptHandler(**dict_0)
            str_0 = 'i"<%Z\\?.'
            name_0 = module_1.Name()
            import_from_0 = None
            str_1 = 'urlopen'
            str_2 = '(K++)Tv@\n|e,(LW\r'
            dict_1 = {str_1: str_1, str_1: str_0, str_1: str_1, str_2: str_1}
            variables_replacer_0 = module_0.VariablesReplacer(dict_1)
            import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
