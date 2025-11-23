import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            var_0 = None
            immutable_list_0 = module_0.ImmutableList()
            str_0 = '2a}'
            var_1 = immutable_list_0.append(var_0)
            dict_0 = {str_0: immutable_list_0, str_0: var_1}
            var_2 = immutable_list_0.to_list()
            callable_0 = None
            optional_0 = immutable_list_0.find(callable_0)
            var_3 = immutable_list_0.map(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
