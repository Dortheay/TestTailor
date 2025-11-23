import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.metaclass as module_1

class Test_Metaclass_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_s_t_0 = module_0.AST()
        metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
