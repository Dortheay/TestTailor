import unittest
import timeout_decorator
import ansible.plugins.inventory.host_list as module_0

class Test_Host_list_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        set_0 = set()
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(set_0)

if __name__ == "__main__":
    unittest.main()
