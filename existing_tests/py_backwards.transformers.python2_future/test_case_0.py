import unittest
import timeout_decorator
import py_backwards.transformers.python2_future as module_0
import typed_ast._ast3 as module_1

class Test_Python2_future_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            python2_future_transformer_0 = module_0.Python2FutureTransformer()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
