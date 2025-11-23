import unittest
import timeout_decorator
import builtins as module_0
import pymonet.box as module_1

class Test_Box_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -1055.6748
            box_0 = module_1.Box(float_0)
            var_0 = box_0.to_try()
            int_0 = 2547
            var_1 = box_0.map(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
