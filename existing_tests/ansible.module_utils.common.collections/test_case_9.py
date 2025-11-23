import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.__len__()
        immutable_dict_1 = module_0.ImmutableDict()
        var_1 = immutable_dict_1.__iter__()
        var_2 = module_0.count(immutable_dict_1)

if __name__ == "__main__":
    unittest.main()
