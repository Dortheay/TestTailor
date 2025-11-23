import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'invalid characters in salt'
        dict_0 = {str_0: str_0}
        immutable_dict_0 = module_0.ImmutableDict(**dict_0)
        immutable_dict_1 = module_0.ImmutableDict(**dict_0)
        str_1 = 'eS}\\FA]v2'
        set_0 = {str_1, str_1, str_1}
        immutable_dict_2 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.difference(set_0)
        list_0 = [var_0, str_1, immutable_dict_2, str_0]
        var_1 = immutable_dict_1.__eq__(list_0)
        list_1 = []
        immutable_dict_3 = module_0.ImmutableDict(*list_1, **dict_0)
        var_2 = immutable_dict_3.__len__()
        var_3 = immutable_dict_2.__repr__()
        var_4 = immutable_dict_2.__eq__(set_0)

if __name__ == "__main__":
    unittest.main()
