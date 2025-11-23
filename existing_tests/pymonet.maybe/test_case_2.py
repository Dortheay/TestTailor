import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            object_0 = module_1.object()
            str_0 = 'm_f?cBmmh'
            float_0 = 1297.882
            bool_0 = False
            maybe_0 = module_0.Maybe(float_0, bool_0)
            var_0 = maybe_0.ap(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
