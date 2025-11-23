import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        list_0 = []
        int_0 = True
        list_1 = [int_0]
        inventory_manager_0 = module_0.InventoryManager(list_1)
        var_0 = inventory_manager_0.parse_source(list_0)

if __name__ == "__main__":
    unittest.main()
