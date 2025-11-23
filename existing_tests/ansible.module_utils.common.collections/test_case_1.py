import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 255.482
            immutable_dict_0 = module_0.ImmutableDict()
            var_0 = immutable_dict_0.union(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
