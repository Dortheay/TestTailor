import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 390
            tuple_0 = (int_0,)
            immutable_dict_0 = module_0.ImmutableDict()
            var_0 = immutable_dict_0.__repr__()
            list_0 = []
            immutable_dict_1 = module_0.ImmutableDict(*list_0)
            var_1 = immutable_dict_1.__getitem__(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
