import unittest
import timeout_decorator
import ansible.plugins.lookup.inventory_hostnames as module_0

class Test_Inventory_hostnames_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            int_0 = -210
            var_0 = lookup_module_0.run(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
