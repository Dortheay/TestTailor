import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            callable_0 = None
            bool_0 = True
            immutable_list_0 = module_0.ImmutableList(bool_0)
            optional_0 = immutable_list_0.find(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
