import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        object_0 = module_1.object()
        set_0 = {object_0, object_0}
        str_0 = 'R fc}ub$Ai2IJyX$)'
        bool_0 = True
        maybe_0 = module_0.Maybe(str_0, bool_0)
        var_0 = maybe_0.filter(set_0)
        bool_1 = False
        maybe_1 = module_0.Maybe(object_0, bool_1)
        var_1 = maybe_1.to_lazy()
        var_2 = maybe_0.to_box()

if __name__ == "__main__":
    unittest.main()
