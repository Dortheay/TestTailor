import unittest
import timeout_decorator
import py_backwards.transformers.return_from_generator as module_0
import typed_ast._ast3 as module_1

class Test_Return_from_generator_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_s_t_0 = None
        return_from_generator_transformer_0 = module_0.ReturnFromGeneratorTransformer(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
