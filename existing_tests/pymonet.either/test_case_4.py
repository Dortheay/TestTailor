import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = -1311
        set_0 = {int_0, int_0}
        list_0 = [int_0]
        left_0 = module_0.Left(list_0)
        var_0 = left_0.map(list_0)
        either_0 = module_0.Either(left_0)
        var_1 = either_0.is_right()
        right_0 = module_0.Right(set_0)
        bool_0 = right_0.is_left()
        list_1 = [int_0, set_0, int_0]
        left_1 = module_0.Left(list_1)
        bool_1 = left_1.is_left()

if __name__ == "__main__":
    unittest.main()
