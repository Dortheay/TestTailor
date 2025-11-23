import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.starred_unpacking as module_1

class Test_Starred_unpacking_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'email.mime.base'
            list_0 = [str_0, str_0]
            list_1 = module_0.List(*list_0)
            a_s_t_0 = module_0.AST()
            starred_unpacking_transformer_0 = module_1.StarredUnpackingTransformer(a_s_t_0)
            list_2 = starred_unpacking_transformer_0.visit_List(list_1)
            starred_unpacking_transformer_1 = None
            list_3 = [starred_unpacking_transformer_1, starred_unpacking_transformer_1]
            a_s_t_1 = module_0.AST(*list_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
