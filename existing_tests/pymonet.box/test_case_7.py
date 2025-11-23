import unittest
import timeout_decorator
import pymonet.box as module_0
import builtins as module_1

class Test_Box_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 713
        box_0 = module_0.Box(int_0)
        var_0 = box_0.to_either()

if __name__ == "__main__":
    unittest.main()
