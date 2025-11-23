import unittest
import timeout_decorator
import py_backwards.utils.tree as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Tree_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'if True:\n    x = 1\n\ny = 2'
            var_0 = module_2.parse(str_0)
            int_0 = 0
            var_1 = var_0.body[int_0]
            var_2 = var_1.body[int_0]
            var_3 = module_0.get_closest_parent_of(var_0, var_2, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
