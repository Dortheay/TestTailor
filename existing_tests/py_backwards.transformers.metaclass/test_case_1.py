import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.metaclass as module_1

class Test_Metaclass_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            module_x_var_0 = module_0.Module()
            a_s_t_0 = module_0.AST()
            list_0 = [a_s_t_0, module_x_var_0, a_s_t_0, a_s_t_0]
            class_def_0 = module_0.ClassDef(*list_0)
            metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_0)
            class_def_1 = metaclass_transformer_0.visit_ClassDef(class_def_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
