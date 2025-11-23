import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bool_0 = True
        inventory_manager_0 = module_0.InventoryManager(bool_0)

if __name__ == "__main__":
    unittest.main()
