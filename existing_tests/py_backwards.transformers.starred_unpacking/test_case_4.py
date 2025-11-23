import unittest
import timeout_decorator
import py_backwards.transformers.starred_unpacking as module_0
import typed_ast._ast3 as module_1

class Test_Starred_unpacking_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'Use/transfo0mer {}"'
        list_0 = [str_0, str_0]
        a_s_t_0 = module_1.AST()
        starred_unpacking_transformer_0 = module_0.StarredUnpackingTransformer(a_s_t_0)
        call_0 = module_1.Call(*list_0)
        call_1 = starred_unpacking_transformer_0.visit_Call(call_0)

if __name__ == "__main__":
    unittest.main()
