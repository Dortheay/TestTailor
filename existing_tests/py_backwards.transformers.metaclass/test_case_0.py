import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.metaclass as module_1

class Test_Metaclass_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'rq$uJ'
            dict_0 = {str_0: str_0}
            module_x_var_0 = module_0.Module(**dict_0)
            a_s_t_0 = module_0.AST()
            metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_0)
            module_x_var_1 = metaclass_transformer_0.visit_Module(module_x_var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
