import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = None
        either_0 = module_0.Either(var_0)

if __name__ == "__main__":
    unittest.main()
