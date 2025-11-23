import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            int_0 = 876
            var_0 = lookup_module_0.parse_kv_args(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
