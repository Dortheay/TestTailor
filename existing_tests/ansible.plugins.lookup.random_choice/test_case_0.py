import unittest
import timeout_decorator
import ansible.plugins.lookup.random_choice as module_0

class Test_Random_choice_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        lookup_module_0 = module_0.LookupModule()
        lookup_module_1 = module_0.LookupModule()
        lookup_module_2 = module_0.LookupModule()

if __name__ == "__main__":
    unittest.main()
