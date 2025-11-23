import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            str_0 = 'start'
            str_1 = 'end'
            str_2 = '10'
            str_3 = 'a'
            str_4 = {str_0: str_3, str_1: str_2}
            var_0 = lookup_module_0.parse_kv_args(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
