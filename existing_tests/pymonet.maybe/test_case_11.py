import unittest
import timeout_decorator
import pymonet.maybe as module_0
import builtins as module_1

class Test_Maybe_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        tuple_0 = ()
        bool_0 = True
        callable_0 = None
        list_0 = [bool_0]
        maybe_0 = module_0.Maybe(list_0, bool_0)
        callable_1 = None
        var_0 = maybe_0.map(callable_1)
        var_1 = maybe_0.bind(callable_0)
        maybe_1 = module_0.Maybe(tuple_0, bool_0)
        bool_1 = False
        maybe_2 = module_0.Maybe(maybe_1, bool_1)
        var_2 = maybe_2.to_box()

if __name__ == "__main__":
    unittest.main()
