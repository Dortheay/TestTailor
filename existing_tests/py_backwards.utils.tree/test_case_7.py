import unittest
import timeout_decorator
import typed_ast.ast3 as module_0
import py_backwards.utils.tree as module_1

class Test_Tree_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '\ndef example_function():\n    x = 1\n    y = 2\n    z = 3\n'
        var_0 = module_0.parse(str_0)
        int_0 = 0
        var_1 = var_0.body[int_0]
        int_1 = 0
        str_1 = 'a = 100'
        var_2 = module_0.parse(str_1)
        var_3 = var_2.body[int_0]
        var_4 = module_0.parse(str_0)
        var_5 = var_4.body[int_0]
        var_6 = [var_3, var_5]
        module_1.replace_at(int_1, var_1, var_6)
        var_7 = var_1.body
        var_8 = len(var_7)
        var_9 = var_1.body[int_0]
        int_2 = 1
        var_10 = var_1.body[int_2]
        var_11 = var_1.body[int_1]
        int_3 = 3
        var_12 = var_1.body[int_3]

if __name__ == "__main__":
    unittest.main()
