import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.base as module_1

class Test_Base_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_s_t_0 = module_0.AST()
        base_node_transformer_0 = module_1.BaseNodeTransformer(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
