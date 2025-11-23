import unittest
import timeout_decorator
import py_backwards.transformers.yield_from as module_0

class Test_Yield_from_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            yield_from_transformer_0 = module_0.YieldFromTransformer()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
