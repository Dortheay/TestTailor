import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            str_0 = '3-7'
            var_0 = lookup_module_0.parse_simple_args(str_0)
            str_1 = '5-invalid-stride'
            var_1 = lookup_module_0.parse_simple_args(str_1)
            str_2 = 'non-numeric'
            var_2 = lookup_module_0.parse_simple_args(str_2)
            str_3 = '0x5-0xA/2:%02x'
            var_3 = lookup_module_0.parse_simple_args(str_3)
            str_4 = '010-020/4:%o'
            var_4 = lookup_module_0.parse_simple_args(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
