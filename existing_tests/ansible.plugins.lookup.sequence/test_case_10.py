import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            int_0 = 876
            set_0 = {lookup_module_0, int_0}
            dict_0 = None
            var_0 = lookup_module_0.run(set_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
