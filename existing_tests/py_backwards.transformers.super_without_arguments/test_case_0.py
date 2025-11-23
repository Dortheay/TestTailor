import unittest
import timeout_decorator
import py_backwards.transformers.super_without_arguments as module_0
import typed_ast._ast3 as module_1

class Test_Super_without_arguments_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            super_without_arguments_transformer_0 = module_0.SuperWithoutArgumentsTransformer()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
