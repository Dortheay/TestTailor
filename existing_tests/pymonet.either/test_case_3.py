import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = -1660
        either_0 = module_0.Either(int_0)
        var_0 = either_0.is_right()

if __name__ == "__main__":
    unittest.main()
