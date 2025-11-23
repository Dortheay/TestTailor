import unittest
import timeout_decorator
import builtins as module_0
import pymonet.box as module_1

class Test_Box_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 2707
            box_0 = module_1.Box(int_0)
            var_0 = box_0.to_maybe()
            callable_0 = None
            var_1 = box_0.bind(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
