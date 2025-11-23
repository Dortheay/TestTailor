import unittest
import timeout_decorator
import py_backwards.transformers.six_moves as module_0

class Test_Six_moves_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            six_moves_transformer_0 = module_0.SixMovesTransformer()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
