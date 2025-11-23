import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bool_0 = True
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_host(bool_0)
        inventory_data_1 = module_0.InventoryData()
        var_1 = inventory_data_1.reconcile_inventory()
        var_2 = inventory_data_1.reconcile_inventory()
        inventory_data_2 = module_0.InventoryData()
        var_3 = inventory_data_1.get_groups_dict()

if __name__ == "__main__":
    unittest.main()
