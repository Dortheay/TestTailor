import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -477
            inventory_manager_0 = module_0.InventoryManager(int_0)
            var_0 = module_0.order_patterns(inventory_manager_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
