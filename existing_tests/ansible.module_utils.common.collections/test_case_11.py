import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '54zO4<AnL2*n#`-`zGQ'
        dict_0 = {str_0: str_0}
        var_0 = module_0.count(dict_0)
        float_0 = 63.49914620268939
        immutable_dict_0 = module_0.ImmutableDict()
        var_1 = module_0.is_string(dict_0)
        var_2 = module_0.is_iterable(float_0)
        list_0 = []
        var_3 = immutable_dict_0.difference(list_0)

if __name__ == "__main__":
    unittest.main()
