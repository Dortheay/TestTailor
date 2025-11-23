import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        bool_0 = True
        bytes_0 = b'B"\xee\xa2\xd3\x94\x14\xea'
        int_0 = -259
        inventory_manager_0 = module_0.InventoryManager(int_0)
        var_0 = inventory_manager_0.get_hosts(bytes_0)
        inventory_manager_1 = module_0.InventoryManager(bool_0)
        bytes_1 = None
        var_1 = inventory_manager_1.remove_restriction()
        int_1 = 1705
        dict_0 = {inventory_manager_1: bool_0, bytes_1: int_1, inventory_manager_1: inventory_manager_1}
        inventory_manager_2 = module_0.InventoryManager(dict_0)

if __name__ == "__main__":
    unittest.main()
