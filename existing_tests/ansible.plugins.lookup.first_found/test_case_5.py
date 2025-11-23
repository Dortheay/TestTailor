import unittest
import timeout_decorator
import ansible.plugins.lookup.first_found as module_0

class Test_First_found_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        set_0 = set()
        lookup_module_0 = module_0.LookupModule(set_0)

if __name__ == "__main__":
    unittest.main()
