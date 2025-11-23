import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            dict_0 = {}
            lookup_module_0 = module_0.LookupModule(**dict_0)
            float_0 = 1.5
            lookup_module_1 = module_0.LookupModule(float_0)
            str_0 = 'c'
            var_0 = lookup_module_0.parse_simple_args(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
