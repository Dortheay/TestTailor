import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'\xeb#UPgq\xd1+\x88}\xe5\x8c'
        tuple_0 = ()
        inventory_manager_0 = module_0.InventoryManager(bytes_0, tuple_0)
        var_0 = inventory_manager_0.list_hosts()
        var_1 = inventory_manager_0.reconcile_inventory()

if __name__ == "__main__":
    unittest.main()
