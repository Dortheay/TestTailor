import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        set_0 = set()
        str_0 = 'D'
        inventory_manager_0 = module_0.InventoryManager(set_0, str_0)
        var_0 = inventory_manager_0.clear_pattern_cache()
        var_1 = inventory_manager_0.remove_restriction()
        var_2 = inventory_manager_0.parse_sources()
        str_1 = ' f%Ady"7\'5z9\''
        bytes_0 = b'\xc7oVk+\xb1\x11)\xc2\x16\x08\xfd\x9bZ\xb5'
        var_3 = inventory_manager_0.list_hosts(bytes_0)
        complex_0 = None
        var_4 = inventory_manager_0.subset(complex_0)
        int_0 = -1
        var_5 = inventory_manager_0.subset(int_0)
        var_6 = inventory_manager_0.list_groups()
        var_7 = inventory_manager_0.clear_pattern_cache()
        var_8 = inventory_manager_0.add_group(str_1)
        str_2 = ''
        var_9 = module_0.split_host_pattern(str_2)
        var_10 = inventory_manager_0.clear_caches()
        str_3 = 'BA\nxj~XJm?C>*Y263NvI'
        var_11 = inventory_manager_0.list_hosts(str_3)
        var_12 = inventory_manager_0.refresh_inventory()

if __name__ == "__main__":
    unittest.main()
