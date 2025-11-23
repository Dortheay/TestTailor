import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'connection_plugins'
            dict_0 = {str_0: str_0}
            immutable_dict_0 = module_0.ImmutableDict(**dict_0)
            var_0 = immutable_dict_0.__len__()
            dict_1 = {}
            list_0 = [dict_1]
            var_1 = module_0.is_sequence(list_0)
            bytes_0 = b'5\n.J\xec\x14\xbd\x85\xa1j\xc7'
            list_1 = [bytes_0]
            var_2 = module_0.count(list_1)
            set_0 = None
            float_0 = -1135.82
            var_3 = module_0.is_sequence(float_0)
            var_4 = module_0.is_iterable(bytes_0, set_0)
            var_5 = immutable_dict_0.difference(dict_0)
            tuple_0 = (immutable_dict_0,)
            var_6 = immutable_dict_0.__hash__()
            var_7 = immutable_dict_0.__eq__(tuple_0)
            list_2 = []
            immutable_dict_1 = module_0.ImmutableDict(*list_2)
            var_8 = immutable_dict_1.__iter__()
            bytes_1 = b'\xcd\xaeR\xa6(s\xa48\xe0\xe2\xfb\xa7\x84\x0f\xaf\x8b\xa6\xe8b'
            immutable_dict_2 = module_0.ImmutableDict()
            var_9 = immutable_dict_2.difference(bytes_1)
            immutable_dict_3 = module_0.ImmutableDict()
            list_3 = [set_0]
            var_10 = immutable_dict_2.__repr__()
            var_11 = immutable_dict_2.__hash__()
            immutable_dict_4 = module_0.ImmutableDict(*list_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
