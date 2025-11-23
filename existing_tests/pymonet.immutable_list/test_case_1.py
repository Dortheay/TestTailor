import unittest
import timeout_decorator
import pymonet.immutable_list as module_0
import builtins as module_1

class Test_Immutable_list_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            object_0 = module_1.object()
            str_0 = '}z\nb,*'
            list_0 = [object_0]
            bool_0 = True
            immutable_list_0 = module_0.ImmutableList(list_0, bool_0)
            bool_1 = immutable_list_0.__eq__(object_0)
            var_0 = immutable_list_0.append(str_0)
            str_1 = 'Y\x0b`r'
            str_2 = "YG}ZvNh^'iLL|Ri< T"
            str_3 = "X\nxx\nn)H'"
            dict_0 = {str_1: str_1, str_2: str_2, str_3: object_0}
            immutable_list_1 = module_0.ImmutableList(dict_0)
            str_4 = immutable_list_1.__str__()
            var_1 = immutable_list_1.__len__()
            str_5 = immutable_list_0.__str__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
