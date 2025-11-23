import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = ''
            immutable_dict_0 = module_0.ImmutableDict()
            var_0 = immutable_dict_0.difference(str_0)
            set_0 = {var_0, immutable_dict_0}
            var_1 = immutable_dict_0.__eq__(set_0)
            dict_0 = {str_0: str_0}
            var_2 = module_0.count(dict_0)
            immutable_dict_1 = module_0.ImmutableDict(**dict_0)
            float_0 = 0.001
            immutable_dict_2 = module_0.ImmutableDict()
            var_3 = module_0.is_string(dict_0)
            var_4 = immutable_dict_2.__hash__()
            var_5 = module_0.is_iterable(float_0)
            list_0 = []
            var_6 = immutable_dict_2.difference(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
