import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            set_0 = set()
            str_0 = 'D'
            inventory_manager_0 = module_0.InventoryManager(set_0, str_0)
            var_0 = inventory_manager_0.list_groups()
            var_1 = inventory_manager_0.subset(set_0)
            str_1 = 'e.dr'
            var_2 = module_0.split_host_pattern(str_1)
            var_3 = inventory_manager_0.list_hosts()
            var_4 = inventory_manager_0.restrict_to_hosts(inventory_manager_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
