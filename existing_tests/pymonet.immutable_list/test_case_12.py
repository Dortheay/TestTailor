import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'JZ+'
            immutable_list_0 = module_0.ImmutableList(str_0)
            object_0 = module_1.object()
            bool_0 = immutable_list_0.__eq__(object_0)
            immutable_list_1 = module_0.ImmutableList()
            var_0 = immutable_list_1.to_list()
            str_1 = immutable_list_1.__str__()
            var_1 = immutable_list_1.unshift(str_1)
            var_2 = immutable_list_1.__add__(var_1)
            bool_1 = False
            dict_0 = None
            var_3 = immutable_list_0.append(dict_0)
            optional_0 = immutable_list_1.find(bool_1)
            int_0 = 581
            var_4 = None
            immutable_list_2 = module_0.ImmutableList()
            var_5 = immutable_list_1.reduce(int_0, var_4)
            var_6 = immutable_list_1.filter(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
