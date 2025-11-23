import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            immutable_list_0 = module_0.ImmutableList()
            callable_0 = None
            var_0 = immutable_list_0.filter(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
