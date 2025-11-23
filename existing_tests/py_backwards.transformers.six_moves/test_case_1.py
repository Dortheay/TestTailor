import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.six_moves as module_1

class Test_Six_moves_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_s_t_0 = module_0.AST()
        str_0 = '-t'
        list_0 = None
        int_0 = 484
        int_1 = -1172
        bool_0 = None
        moved_module_0 = module_1.MovedModule(int_1, bool_0)
        six_moves_transformer_0 = module_1.SixMovesTransformer(a_s_t_0)
        moved_attribute_0 = module_1.MovedAttribute(str_0, list_0, int_0)
        six_moves_transformer_1 = module_1.SixMovesTransformer(a_s_t_0)
        list_1 = None
        six_moves_transformer_2 = module_1.SixMovesTransformer(a_s_t_0)
        bool_1 = False
        str_1 = None
        bool_2 = True
        dict_0 = {str_0: moved_attribute_0, str_0: moved_attribute_0, str_1: bool_2}
        list_2 = [str_1, six_moves_transformer_2]
        list_3 = [str_1, six_moves_transformer_0, list_2, bool_1]
        moved_module_1 = module_1.MovedModule(dict_0, list_3, dict_0)
        moved_module_2 = module_1.MovedModule(list_1, bool_1)
        bytes_0 = None
        moved_attribute_1 = module_1.MovedAttribute(six_moves_transformer_1, moved_module_2, bytes_0)
        six_moves_transformer_3 = module_1.SixMovesTransformer(a_s_t_0)

if __name__ == "__main__":
    unittest.main()
