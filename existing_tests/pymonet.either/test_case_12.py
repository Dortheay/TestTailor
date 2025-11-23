import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = None
            either_0 = module_0.Either(var_0)
            either_1 = module_0.Either(either_0)
            list_0 = None
            var_1 = either_0.to_box()
            var_2 = either_1.ap(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
