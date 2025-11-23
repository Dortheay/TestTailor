import unittest
import timeout_decorator
import typed_ast._ast3 as module_0
import py_backwards.transformers.dict_unpacking as module_1

class Test_Dict_unpacking_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = None
            a_s_t_0 = module_0.AST()
            dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
            var_0 = dict_unpacking_transformer_0.visit_Dict(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
