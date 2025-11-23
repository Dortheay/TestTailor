import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.reset()
            var_1 = lookup_module_0.sanity_check()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
