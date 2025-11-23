import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            immutable_list_0 = module_0.ImmutableList()
            str_0 = immutable_list_0.__str__()
            object_0 = module_1.object()
            bool_0 = False
            immutable_list_1 = module_0.ImmutableList(object_0, bool_0)
            var_0 = immutable_list_1.filter(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
