import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        bool_0 = False
        inventory_manager_0 = module_0.InventoryManager(bool_0)
        var_0 = inventory_manager_0.get_groups_dict()

if __name__ == "__main__":
    unittest.main()
