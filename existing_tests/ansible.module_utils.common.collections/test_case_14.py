import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'Ua\x0c\\_,\t\riDm6\x0bG&W5'
        dict_0 = {str_0: str_0}
        immutable_dict_0 = module_0.ImmutableDict(**dict_0)
        var_0 = immutable_dict_0.__iter__()
        immutable_dict_1 = None
        float_0 = 4539.32
        var_1 = module_0.is_iterable(immutable_dict_1, float_0)

if __name__ == "__main__":
    unittest.main()
