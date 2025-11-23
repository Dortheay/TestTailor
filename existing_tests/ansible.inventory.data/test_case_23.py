import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            inventory_data_0 = module_0.InventoryData()
            var_0 = inventory_data_0.get_groups_dict()
            var_1 = inventory_data_0.get_groups_dict()
            var_2 = inventory_data_0.reconcile_inventory()
            str_0 = 'UNIXCONFDR'
            var_3 = inventory_data_0.add_host(str_0)
            inventory_data_1 = module_0.InventoryData()
            var_4 = inventory_data_1.deserialize(inventory_data_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
