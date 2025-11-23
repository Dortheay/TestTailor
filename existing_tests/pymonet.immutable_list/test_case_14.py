import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            int_0 = True
            str_0 = '8{-guTig['
            immutable_list_0 = module_0.ImmutableList(str_0)
            var_0 = immutable_list_0.unshift(int_0)
            callable_0 = None
            var_1 = None
            var_2 = immutable_list_0.reduce(callable_0, var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
