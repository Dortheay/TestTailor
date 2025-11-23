import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        float_0 = 3020.83
        list_0 = [float_0, float_0]
        right_0 = module_0.Right(list_0)
        bool_0 = right_0.is_left()
        either_0 = module_0.Either(float_0)
        var_0 = either_0.is_right()

if __name__ == "__main__":
    unittest.main()
