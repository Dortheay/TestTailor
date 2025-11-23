import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.__iter__()
        var_1 = module_0.count(immutable_dict_0)

if __name__ == "__main__":
    unittest.main()
