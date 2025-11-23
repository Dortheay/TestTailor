import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            list_0 = None
            list_1 = [list_0]
            alias_0 = module_1.alias(*list_1)
            dict_0 = {}
            variables_replacer_0 = module_0.VariablesReplacer(dict_0)
            alias_1 = variables_replacer_0.visit_alias(alias_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
