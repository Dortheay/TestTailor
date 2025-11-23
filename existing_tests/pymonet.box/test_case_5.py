import unittest
import timeout_decorator
import pymonet.box as module_0
import builtins as module_1

class Test_Box_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = None
        box_0 = module_0.Box(var_0)

if __name__ == "__main__":
    unittest.main()
