import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_s_t_0 = module_0.AST()
        iterable_0 = module_1.find_variables(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
