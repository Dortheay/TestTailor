import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.dict_unpacking as module_1

class Test_Dict_unpacking_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = None
            tuple_0 = (float_0,)
            list_0 = [tuple_0]
            dict_0 = module_0.Dict(*list_0)
            a_s_t_0 = module_0.AST()
            dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
            var_0 = dict_unpacking_transformer_0.visit_Dict(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
