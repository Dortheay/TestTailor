import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '\ndef example():\n    let(x)\n    x += 1\n    y = 2\n'
            var_0 = module_2.parse(str_0)
            iterable_0 = module_0.find_variables(var_0)
            var_1 = list(iterable_0)
            var_2 = var_0.body[var_1]
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
