import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        list_0 = []
        list_1 = [list_0, list_0, list_0]
        bool_0 = False
        maybe_0 = module_0.Maybe(list_1, bool_0)
        var_0 = maybe_0.to_try()

if __name__ == "__main__":
    unittest.main()
