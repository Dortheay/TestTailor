import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        set_0 = set()
        str_0 = 'D'
        inventory_manager_0 = module_0.InventoryManager(set_0, str_0)
        float_0 = 548.86977
        var_0 = inventory_manager_0.parse_source(float_0)
        var_1 = inventory_manager_0.clear_pattern_cache()
        var_2 = inventory_manager_0.list_groups()
        var_3 = inventory_manager_0.remove_restriction()
        var_4 = inventory_manager_0.parse_sources()
        str_1 = ' f%Ady"7\'5z9\''
        var_5 = module_0.split_host_pattern(str_1)
        int_0 = 0
        var_6 = inventory_manager_0.subset(int_0)
        var_7 = inventory_manager_0.list_groups()
        var_8 = inventory_manager_0.clear_pattern_cache()
        var_9 = inventory_manager_0.add_group(str_1)
        list_0 = []
        str_2 = '[=y'
        var_10 = module_0.split_host_pattern(list_0)
        var_11 = inventory_manager_0.list_hosts()
        float_1 = -186.1
        str_3 = "R~'N\n!"
        inventory_manager_1 = module_0.InventoryManager(float_1, str_3)
        var_12 = inventory_manager_1.refresh_inventory()
        var_13 = inventory_manager_0.refresh_inventory()
        inventory_manager_2 = module_0.InventoryManager(str_2)
        var_14 = inventory_manager_2.restrict_to_hosts(list_0)
        var_15 = inventory_manager_2.parse_source(list_0)

if __name__ == "__main__":
    unittest.main()
