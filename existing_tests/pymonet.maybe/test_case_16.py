import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        tuple_0 = None
        set_0 = {tuple_0}
        bool_0 = True
        maybe_0 = module_0.Maybe(set_0, bool_0)
        var_0 = maybe_0.to_validation()

if __name__ == "__main__":
    unittest.main()
