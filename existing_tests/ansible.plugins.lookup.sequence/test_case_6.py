import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            lookup_module_0 = module_0.LookupModule(bool_0)
            str_0 = 'J@f2A]A'
            list_0 = [str_0, bool_0]
            dict_0 = {lookup_module_0: list_0}
            var_0 = lookup_module_0.parse_kv_args(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
