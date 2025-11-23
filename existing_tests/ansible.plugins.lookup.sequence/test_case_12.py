import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            dict_0 = {}
            lookup_module_0 = module_0.LookupModule(**dict_0)
            var_0 = lookup_module_0.generate_sequence()
            str_0 = '\\*D[\x0bya=/Y'
            dict_1 = {lookup_module_0: lookup_module_0, str_0: dict_0}
            var_1 = lookup_module_0.run(str_0, dict_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
