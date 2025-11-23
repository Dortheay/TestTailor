import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            callable_0 = None
            var_0 = None
            immutable_list_0 = module_0.ImmutableList()
            str_0 = immutable_list_0.__str__()
            bool_0 = True
            immutable_list_1 = module_0.ImmutableList(bool_0)
            var_1 = immutable_list_1.append(var_0)
            immutable_list_2 = module_0.ImmutableList()
            str_1 = immutable_list_1.__str__()
            var_2 = immutable_list_2.__add__(var_1)
            str_2 = immutable_list_2.__str__()
            var_3 = immutable_list_0.to_list()
            optional_0 = immutable_list_2.find(callable_0)
            var_4 = immutable_list_0.map(var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
