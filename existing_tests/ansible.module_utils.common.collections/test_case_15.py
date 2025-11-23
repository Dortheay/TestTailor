import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        immutable_dict_0 = module_0.ImmutableDict()
        str_0 = '54zO4<AnL2*n#`-`zGQ'
        dict_0 = {str_0: str_0}
        float_0 = 0.001
        immutable_dict_1 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.__repr__()
        var_1 = module_0.is_string(dict_0)
        var_2 = immutable_dict_1.__hash__()
        var_3 = module_0.is_iterable(float_0)
        var_4 = immutable_dict_1.__len__()
        set_0 = {float_0, var_2}
        list_0 = [float_0, var_1, str_0]
        var_5 = module_0.is_sequence(set_0, list_0)
        var_6 = immutable_dict_1.__repr__()

if __name__ == "__main__":
    unittest.main()
