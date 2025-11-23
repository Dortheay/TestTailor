import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            str_0 = 'start'
            str_1 = 'end'
            str_2 = 'stride'
            str_3 = 'format'
            str_4 = '0x10'
            str_5 = '20'
            str_6 = '2'
            str_7 = '%02d'
            str_8 = {str_0: str_4, str_1: str_5, str_2: str_6, str_3: str_7}
            var_0 = lookup_module_0.parse_kv_args(str_8)
            str_9 = 'unknown'
            str_10 = 'value'
            str_11 = {str_9: str_10}
            var_1 = lookup_module_0.parse_kv_args(str_11)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
