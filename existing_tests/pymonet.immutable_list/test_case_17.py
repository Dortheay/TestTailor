import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = True
        immutable_list_0 = module_0.ImmutableList(bool_0)
        var_0 = immutable_list_0.unshift(bool_0)

if __name__ == "__main__":
    unittest.main()
