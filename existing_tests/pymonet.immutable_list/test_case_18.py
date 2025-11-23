import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'K\tu<syQO#s5JK EQG\\'
        dict_0 = {str_0: str_0, str_0: str_0}
        object_0 = module_1.object()
        str_1 = '|SYt\\^=aj3R'
        immutable_list_0 = module_0.ImmutableList(str_1)
        var_0 = immutable_list_0.__len__()
        immutable_list_1 = module_0.ImmutableList()
        var_1 = None
        var_2 = immutable_list_1.append(var_1)
        var_3 = immutable_list_1.unshift(var_1)
        immutable_list_2 = module_0.ImmutableList(dict_0, var_3)
        bool_0 = immutable_list_2.__eq__(object_0)
        immutable_list_3 = module_0.ImmutableList()

if __name__ == "__main__":
    unittest.main()
