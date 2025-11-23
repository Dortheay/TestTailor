import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.starred_unpacking as module_1

class Test_Starred_unpacking_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            call_0 = None
            a_s_t_0 = module_0.AST()
            starred_unpacking_transformer_0 = module_1.StarredUnpackingTransformer(a_s_t_0)
            call_1 = starred_unpacking_transformer_0.visit_Call(call_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
