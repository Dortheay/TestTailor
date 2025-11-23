import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = False
            immutable_list_0 = module_0.ImmutableList(bool_0, bool_0)
            int_0 = 332
            immutable_list_1 = module_0.ImmutableList(int_0)
            immutable_list_2 = module_0.ImmutableList()
            tuple_0 = None
            var_0 = immutable_list_0.unshift(tuple_0)
            var_1 = immutable_list_0.to_list()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
