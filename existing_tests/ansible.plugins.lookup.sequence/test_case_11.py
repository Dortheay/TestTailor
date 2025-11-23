import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'dummy_var'
            str_1 = {str_0: str_0}
            var_0 = {}
            lookup_module_0 = module_0.LookupModule()
            var_1 = lookup_module_0.run(str_0, str_1, **var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
