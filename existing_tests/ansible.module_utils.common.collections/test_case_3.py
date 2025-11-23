import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            immutable_dict_0 = None
            var_0 = module_0.count(immutable_dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
