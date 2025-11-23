import unittest
import timeout_decorator
import ansible.plugins.lookup.subelements as module_0

class Test_Subelements_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = None
            dict_0 = None
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(float_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
