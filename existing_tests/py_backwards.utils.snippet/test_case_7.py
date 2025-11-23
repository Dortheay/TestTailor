import unittest
import timeout_decorator
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1
import typed_ast.ast3 as module_2

class Test_Snippet_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            name_0 = module_1.Name()
            module_0.let(name_0)
            except_handler_0 = module_1.ExceptHandler()
            str_0 = '"6*G\\Ojqt'
            snippet_0 = module_0.snippet(str_0)
            list_0 = snippet_0.get_body()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
