import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            callable_0 = None
            str_0 = '@|)5tu7A+&|\x0b}$>E%DN+'
            immutable_list_0 = module_0.ImmutableList()
            var_0 = immutable_list_0.append(str_0)
            bool_0 = False
            immutable_list_1 = module_0.ImmutableList(var_0, bool_0)
            optional_0 = immutable_list_1.find(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
