import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        bytes_0 = b'\xeb#UPgq\xd1+\x88}\xe5\x8c'
        tuple_0 = ()
        inventory_manager_0 = module_0.InventoryManager(bytes_0, tuple_0)
        var_0 = inventory_manager_0.parse_source(inventory_manager_0)
        var_1 = inventory_manager_0.list_hosts()
        var_2 = inventory_manager_0.reconcile_inventory()
        var_3 = inventory_manager_0.list_hosts()
        var_4 = inventory_manager_0.refresh_inventory()
        bool_0 = True
        inventory_manager_1 = module_0.InventoryManager(bool_0)

if __name__ == "__main__":
    unittest.main()
