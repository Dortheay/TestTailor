import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '\n        Transform Either to Try.\n\n        :returns: resolved Try monad with previous value. Right is resolved successfully, Left not.\n        :rtype: Box[A]\n        '
        callable_0 = None
        object_0 = module_1.object()
        object_1 = module_1.object()
        bool_0 = True
        maybe_0 = module_0.Maybe(str_0, bool_0)
        var_0 = maybe_0.filter(callable_0)
        var_1 = maybe_0.to_either()

if __name__ == "__main__":
    unittest.main()
