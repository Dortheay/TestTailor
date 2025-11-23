import unittest
import timeout_decorator
import ansible.plugins.inventory.advanced_host_list as module_0

class Test_Advanced_host_list_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        inventory_module_0 = module_0.InventoryModule()

if __name__ == "__main__":
    unittest.main()
