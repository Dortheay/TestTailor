import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = False
            immutable_dict_0 = module_0.ImmutableDict()
            var_0 = immutable_dict_0.__eq__(bool_0)
            str_0 = 'iyt@Mx@Kmu3iag\t'
            var_1 = module_0.count(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
