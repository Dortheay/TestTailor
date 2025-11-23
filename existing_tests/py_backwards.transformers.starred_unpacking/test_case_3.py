import unittest
import timeout_decorator
import py_backwards.transformers.starred_unpacking as module_0
import typed_ast._ast3 as module_1

class Test_Starred_unpacking_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_s_t_0 = None
        starred_unpacking_transformer_0 = module_0.StarredUnpackingTransformer(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
