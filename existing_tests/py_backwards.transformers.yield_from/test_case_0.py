import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.yield_from as module_1

class Test_Yield_from_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_s_t_0 = module_0.AST()
        yield_from_transformer_0 = module_1.YieldFromTransformer(a_s_t_0)
        a_s_t_1 = yield_from_transformer_0.visit(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
