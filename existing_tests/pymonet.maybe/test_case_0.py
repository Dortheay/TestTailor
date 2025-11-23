import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            str_0 = '>w_ocUtVTr'
            list_0 = [bool_0, bool_0]
            str_1 = '/7'
            bool_1 = True
            maybe_0 = module_0.Maybe(str_1, bool_1)
            var_0 = maybe_0.to_try()
            maybe_1 = module_0.Maybe(list_0, bool_0)
            var_1 = maybe_1.map(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
