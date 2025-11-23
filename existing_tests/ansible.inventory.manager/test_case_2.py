import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            inventory_manager_0 = module_0.InventoryManager(bool_0)
            var_0 = inventory_manager_0.clear_pattern_cache()
            var_1 = inventory_manager_0.get_groups_dict()
            int_0 = -1126
            bytes_0 = b'{'
            var_2 = inventory_manager_0.add_host(int_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
