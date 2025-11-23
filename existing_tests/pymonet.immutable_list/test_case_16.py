import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        object_0 = module_1.object()
        immutable_list_0 = module_0.ImmutableList()
        bool_0 = immutable_list_0.__eq__(object_0)

if __name__ == "__main__":
    unittest.main()
