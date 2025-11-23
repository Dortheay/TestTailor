import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.metaclass as module_1

class Test_Metaclass_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            a_s_t_0 = module_0.AST()
            bytes_0 = None
            list_0 = [bytes_0, bytes_0, bytes_0]
            class_def_0 = module_0.ClassDef(*list_0)
            a_s_t_1 = module_0.AST()
            metaclass_transformer_0 = module_1.MetaclassTransformer(a_s_t_1)
            class_def_1 = metaclass_transformer_0.visit_ClassDef(class_def_0)
            metaclass_transformer_1 = module_1.MetaclassTransformer(a_s_t_0)
            module_x_var_0 = module_0.Module()
            class_def_2 = metaclass_transformer_0.visit_ClassDef(class_def_1)
            class_def_3 = metaclass_transformer_0.visit_ClassDef(class_def_1)
            module_x_var_1 = metaclass_transformer_0.visit_Module(module_x_var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
