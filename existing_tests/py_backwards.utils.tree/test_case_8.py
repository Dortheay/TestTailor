import unittest
import timeout_decorator
import typed_ast.ast3 as module_0
import py_backwards.utils.tree as module_1

class Test_Tree_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'x = 1\ny = 2'
        var_0 = module_0.parse(str_0)
        int_0 = 1
        var_1 = var_0.body[int_0]
        var_2 = var_0
        a_s_t_0 = module_1.get_parent(var_0, var_1)
        bool_0 = True
        a_s_t_1 = module_1.get_parent(var_0, var_1, bool_0)

if __name__ == "__main__":
    unittest.main()
