import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '\x0cm_N$'
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.parse_simple_args(str_0)
            int_0 = 907
            var_1 = lookup_module_0.parse_kv_args(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
