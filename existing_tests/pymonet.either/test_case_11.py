import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 2340
            str_0 = 'Vm7t!&9qa\rogi('
            bool_0 = False
            either_0 = module_0.Either(bool_0)
            var_0 = either_0.to_box()
            var_1 = either_0.case(int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
