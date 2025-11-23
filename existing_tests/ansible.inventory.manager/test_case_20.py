import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        float_0 = -2194.71871
        inventory_manager_0 = module_0.InventoryManager(float_0)
        var_0 = inventory_manager_0.reconcile_inventory()
        var_1 = inventory_manager_0.clear_caches()

if __name__ == "__main__":
    unittest.main()
