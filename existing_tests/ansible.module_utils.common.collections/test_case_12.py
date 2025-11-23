import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.__len__()
        immutable_dict_1 = module_0.ImmutableDict()
        list_0 = [immutable_dict_1, immutable_dict_1, immutable_dict_0]
        var_1 = module_0.is_sequence(list_0)

if __name__ == "__main__":
    unittest.main()
