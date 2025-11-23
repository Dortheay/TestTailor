import unittest
import timeout_decorator
import py_backwards.utils.tree as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Tree_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            list_0 = []
            int_0 = 215
            a_s_t_0 = module_1.AST(*list_0)
            module_0.insert_at(int_0, a_s_t_0, a_s_t_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
