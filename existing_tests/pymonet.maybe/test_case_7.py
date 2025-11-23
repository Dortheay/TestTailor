import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = None
        bool_0 = True
        maybe_0 = module_0.Maybe(var_0, bool_0)

if __name__ == "__main__":
    unittest.main()
