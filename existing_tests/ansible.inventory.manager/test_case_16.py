import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'F2'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
