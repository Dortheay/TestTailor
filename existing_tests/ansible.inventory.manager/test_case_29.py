import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        set_0 = set()
        str_0 = 'D'
        inventory_manager_0 = module_0.InventoryManager(set_0, str_0)
        var_0 = inventory_manager_0.clear_pattern_cache()
        var_1 = inventory_manager_0.remove_restriction()
        var_2 = inventory_manager_0.parse_sources()
        str_1 = ' 8*g\x0c1TSJCh'
        inventory_manager_1 = module_0.InventoryManager(str_1)
        var_3 = inventory_manager_0.list_hosts()
        int_0 = 722
        var_4 = inventory_manager_1.remove_restriction()
        str_2 = ' f%Ady"7\'5z9\''
        bytes_0 = b'\xc7oVk+\xb1\x11)\xc2\x16\x08\xfd\x9bZ\x8e\xb5'
        var_5 = inventory_manager_0.list_hosts(bytes_0)
        var_6 = inventory_manager_0.list_groups()
        var_7 = inventory_manager_0.parse_sources(int_0)
        var_8 = inventory_manager_0.clear_pattern_cache()
        var_9 = inventory_manager_0.add_group(str_2)
        str_3 = '^model bam\r.*fML'
        str_4 = 'QXt,ve;D~XC,\t'
        var_10 = inventory_manager_0.get_host(str_3)
        var_11 = module_0.split_host_pattern(str_4)
        var_12 = inventory_manager_0.list_hosts()
        var_13 = inventory_manager_0.refresh_inventory()

if __name__ == "__main__":
    unittest.main()
