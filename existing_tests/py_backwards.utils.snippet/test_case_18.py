import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'urllib.error'
        callable_0 = None
        snippet_0 = module_1.snippet(callable_0)
        dict_0 = {str_0: snippet_0}
        a_s_t_0 = module_0.AST(**dict_0)
        str_1 = 'JDq||n3[[p\x0b'
        dict_1 = {str_1: a_s_t_0}
        module_1.extend_tree(a_s_t_0, dict_1)

if __name__ == "__main__":
    unittest.main()
