import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = 1192
            immutable_list_0 = module_0.ImmutableList()
            var_0 = immutable_list_0.map(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
