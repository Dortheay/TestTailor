import unittest
import timeout_decorator
import ansible.plugins.lookup.varnames as module_0

class Test_Varnames_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            list_0 = [dict_0]
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(dict_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
