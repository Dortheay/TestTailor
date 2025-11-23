import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        inventory_data_0 = module_0.InventoryData()
        var_0 = inventory_data_0.get_groups_dict()
        str_0 = '\x0cN'
        var_1 = inventory_data_0.add_host(str_0)
        var_2 = inventory_data_0.reconcile_inventory()
        var_3 = inventory_data_0.add_group(str_0)
        str_1 = '*'
        var_4 = inventory_data_0.get_host(str_1)
        var_5 = inventory_data_0.add_group(str_0)
        var_6 = inventory_data_0.reconcile_inventory()
        var_7 = inventory_data_0.reconcile_inventory()
        inventory_data_1 = module_0.InventoryData()
        var_8 = inventory_data_0.serialize()

if __name__ == "__main__":
    unittest.main()
