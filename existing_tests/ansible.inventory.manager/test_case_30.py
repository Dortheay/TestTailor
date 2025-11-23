import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        bool_0 = True
        bytes_0 = b'\xcct\xfc+\xf7\xfe\xe1'
        inventory_manager_0 = module_0.InventoryManager(bytes_0)
        inventory_manager_1 = module_0.InventoryManager(inventory_manager_0)
        var_0 = inventory_manager_0.remove_restriction()
        float_0 = 1327.0
        var_1 = inventory_manager_0.parse_source(float_0)
        var_2 = inventory_manager_1.get_host(bool_0)
        var_3 = inventory_manager_1.refresh_inventory()
        var_4 = inventory_manager_1.reconcile_inventory()
        var_5 = inventory_manager_0.remove_restriction()
        str_0 = 'P'
        var_6 = inventory_manager_1.parse_source(str_0)
        str_1 = '-'
        var_7 = inventory_manager_1.get_hosts(inventory_manager_0, str_1, str_0)
        var_8 = inventory_manager_1.refresh_inventory()

if __name__ == "__main__":
    unittest.main()
