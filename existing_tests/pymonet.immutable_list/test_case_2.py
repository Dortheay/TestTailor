import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            tuple_0 = None
            immutable_list_0 = module_0.ImmutableList()
            str_0 = immutable_list_0.__str__()
            bool_0 = False
            immutable_list_1 = module_0.ImmutableList(bool_0)
            var_0 = immutable_list_1.unshift(tuple_0)
            bool_1 = True
            list_0 = [tuple_0, var_0, immutable_list_1, bool_1]
            bool_2 = True
            immutable_list_2 = module_0.ImmutableList(list_0, bool_2)
            var_1 = immutable_list_2.__len__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
