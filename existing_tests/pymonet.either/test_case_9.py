import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'IIVN(<W'
        int_0 = -2196
        list_0 = [str_0, str_0, int_0]
        right_0 = module_0.Right(list_0)
        var_0 = right_0.to_maybe()

if __name__ == "__main__":
    unittest.main()
