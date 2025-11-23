import unittest
import timeout_decorator
import py_backwards.utils.tree as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Tree_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -2505
            a_s_t_0 = None
            list_0 = []
            module_0.insert_at(int_0, a_s_t_0, list_0)
            int_1 = 1332
            a_s_t_1 = module_1.AST()
            module_0.insert_at(int_1, a_s_t_1, a_s_t_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
