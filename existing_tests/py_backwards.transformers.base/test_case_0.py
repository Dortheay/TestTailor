import unittest
import timeout_decorator
import py_backwards.transformers.base as module_0
import typed_ast.ast3 as module_1
import typed_ast._ast3 as module_2

class Test_Base_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            base_transformer_0 = module_0.BaseTransformer()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
