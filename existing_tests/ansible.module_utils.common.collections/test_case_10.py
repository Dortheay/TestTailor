import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'eS}\\FA]v2'
        set_0 = {str_0, str_0, str_0}
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.__repr__()
        var_1 = immutable_dict_0.__eq__(set_0)

if __name__ == "__main__":
    unittest.main()
