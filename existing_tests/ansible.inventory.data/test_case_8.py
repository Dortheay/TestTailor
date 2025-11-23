import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_groups_dict()
        str_0 = 's;'
        var_1 = inventory_data_0.add_group(str_0)
        var_2 = inventory_data_0.remove_group(str_0)
        str_1 = ''
        var_3 = inventory_data_0.get_host(str_1)
        var_4 = inventory_data_0.reconcile_inventory()
        inventory_data_1 = module_0.InventoryData()
        inventory_data_2 = module_0.InventoryData()
        inventory_data_3 = module_0.InventoryData()
        inventory_data_4 = module_0.InventoryData()
        var_5 = inventory_data_2.serialize()

if __name__ == "__main__":
    unittest.main()
