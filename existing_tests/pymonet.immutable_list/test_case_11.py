import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            callable_0 = None
            var_0 = None
            str_0 = "5Z\x0c38)bNA!0'\r4"
            bool_0 = True
            immutable_list_0 = module_0.ImmutableList(str_0, bool_0)
            var_1 = immutable_list_0.reduce(callable_0, var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
