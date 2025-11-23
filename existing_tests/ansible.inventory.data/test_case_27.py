import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            inventory_data_0 = module_0.InventoryData()
            inventory_data_1 = module_0.InventoryData()
            var_0 = inventory_data_1.get_groups_dict()
            str_0 = 'all'
            var_1 = inventory_data_1.add_host(str_0)
            var_2 = inventory_data_1.reconcile_inventory()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
