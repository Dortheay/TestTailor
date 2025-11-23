import unittest
import timeout_decorator
import py_backwards.transformers.python2_future as module_0
import typed_ast._ast3 as module_1

class Test_Python2_future_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            module_x_var_0 = module_1.Module()
            a_s_t_0 = module_1.AST()
            python2_future_transformer_0 = module_0.Python2FutureTransformer(a_s_t_0)
            module_x_var_1 = python2_future_transformer_0.visit_Module(module_x_var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
