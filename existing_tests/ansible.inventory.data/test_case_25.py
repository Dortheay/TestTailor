import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            inventory_data_0 = module_0.InventoryData()
            inventory_data_1 = module_0.InventoryData()
            var_0 = inventory_data_1.get_groups_dict()
            str_0 = 's;'
            var_1 = inventory_data_1.add_host(str_0)
            var_2 = inventory_data_1.reconcile_inventory()
            var_3 = inventory_data_1.remove_group(str_0)
            str_1 = "p'\x0b#~{7V"
            var_4 = inventory_data_1.get_host(str_1)
            var_5 = inventory_data_1.reconcile_inventory()
            dict_0 = {}
            var_6 = inventory_data_0.deserialize(dict_0)
            inventory_data_2 = module_0.InventoryData()
            inventory_data_3 = module_0.InventoryData()
            inventory_data_4 = module_0.InventoryData()
            inventory_data_5 = module_0.InventoryData()
            inventory_data_6 = module_0.InventoryData()
            var_7 = inventory_data_4.serialize()
            int_0 = 0
            var_8 = inventory_data_5.add_group(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
