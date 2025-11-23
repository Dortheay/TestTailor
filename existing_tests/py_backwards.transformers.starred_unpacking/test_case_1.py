import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.starred_unpacking as module_1

class Test_Starred_unpacking_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            a_s_t_0 = None
            starred_unpacking_transformer_0 = module_1.StarredUnpackingTransformer(a_s_t_0)
            starred_unpacking_transformer_1 = module_1.StarredUnpackingTransformer(a_s_t_0)
            list_0 = module_0.List()
            list_1 = starred_unpacking_transformer_1.visit_List(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
