import unittest
import timeout_decorator
import pymonet.box as module_0
import builtins as module_1

class Test_Box_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = ''
        box_0 = module_0.Box(str_0)
        var_0 = box_0.to_lazy()

if __name__ == "__main__":
    unittest.main()
