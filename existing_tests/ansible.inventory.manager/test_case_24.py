import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        bytes_0 = b"\xe4\x01\xfc\xfb\x08\x93\x8cv'hc2\xa3\x04\x04\xe0"
        inventory_manager_0 = module_0.InventoryManager(bytes_0)
        var_0 = inventory_manager_0.list_groups()

if __name__ == "__main__":
    unittest.main()
