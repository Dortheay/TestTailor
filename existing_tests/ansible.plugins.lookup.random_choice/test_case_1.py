import unittest
import timeout_decorator
import ansible.plugins.lookup.random_choice as module_0

class Test_Random_choice_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        list_0 = []
        lookup_module_0 = module_0.LookupModule()
        lookup_module_1 = module_0.LookupModule()
        var_0 = lookup_module_1.run(list_0, lookup_module_0)

if __name__ == "__main__":
    unittest.main()
