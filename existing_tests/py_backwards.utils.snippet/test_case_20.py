import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = '\ndef test_function():\n    extend(some_variable)\n    print("Hello")\n'
        var_0 = module_2.parse(str_0)
        str_1 = 'some_variable'
        str_2 = 'x = 1\ny = 2'
        var_1 = module_2.parse(str_2)
        var_2 = var_1.body
        var_3 = {str_1: var_2}
        module_1.extend_tree(var_0, var_3)
        int_0 = 0
        var_4 = var_0.body[int_0]
        var_5 = var_4.body
        var_6 = len(var_5)
        var_7 = var_5[int_0]
        int_1 = 1
        var_8 = var_5[int_1]
        int_2 = 2
        var_9 = var_5[int_2]
        var_10 = var_5[int_2]
        var_11 = var_10.value

if __name__ == "__main__":
    unittest.main()
