import unittest
import timeout_decorator
import py_backwards.utils.tree as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Tree_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            a_s_t_0 = module_1.AST()
            var_0 = module_0.get_closest_parent_of(a_s_t_0, a_s_t_0, a_s_t_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
